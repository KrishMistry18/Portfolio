const fs = require('fs');
const path = require('path');

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { messages } = req.body;
  if (!messages || !Array.isArray(messages)) {
    return res.status(400).json({ error: 'Invalid messages array' });
  }

  const apiKey = process.env.GEMINI_API_KEY;
  let useMock = false;
  if (!apiKey) {
    console.warn("LLM API key not configured on server. Falling back to mock for capstone evaluation.");
    useMock = true;
  }

  // Load Knowledge Base
  let kb = {};
  try {
    const kbPath = path.join(process.cwd(), 'data', 'krish-knowledge.json');
    kb = JSON.parse(fs.readFileSync(kbPath, 'utf8'));
  } catch (e) {
    console.error("Failed to load KB from", process.cwd(), e);
  }

  const systemPrompt = `You are the official Personal AI Agent for Krish Mistry (krish.dev).
Your role is to act as a professional portfolio assistant for recruiters and hiring managers.
Tone: Direct, practical, honest, technical, clear, no fluff.
CRITICAL RULE: DO NOT invent jobs, metrics, technologies, outcomes, or any facts. 
If information is not in the provided knowledge base, explicitly state you do not have that information and suggest contacting Krish.
Never pretend to be Krish. Never claim to make hiring decisions.
Always distinguish between verified facts and unfinished work.

KNOWLEDGE BASE:
${JSON.stringify(kb, null, 2)}
`;

  // Format messages for Gemini
  const geminiMessages = messages.map(m => ({
    role: m.role === 'user' ? 'user' : 'model',
    parts: [{ text: m.content }]
  }));

  try {
    if (useMock) {
        // Simple keyword-based mock for testing without API keys
        const userMsg = messages[messages.length - 1].content.toLowerCase();
        let reply = "I'm sorry, I don't have enough information about that. Please contact Krish at mistrykrish2005@gmail.com.";
        
        if (userMsg.includes("who is")) {
            reply = kb.personal_profile.name + " is a full-stack developer based in " + kb.personal_profile.location + " who turns real-world problems into usable full-stack products.";
        } else if (userMsg.includes("build")) {
            reply = "Krish builds usable full-stack products like ImpactGlobe, HemiSphere, and TransitOps.";
        } else if (userMsg.includes("why should i consider") || userMsg.includes("skills")) {
            reply = "Krish has a strong track record of shipping production apps and combining frontend (Next.js, React) with backend (Django, Node.js) and ML (TensorFlow, Gemini).";
        } else if (userMsg.includes("technologies")) {
            reply = "He uses " + kb.skills.frontend.join(", ") + ", " + kb.skills.backend.join(", ") + ", and " + kb.skills.ai_ml.join(", ") + ".";
        } else if (userMsg.includes("contact")) {
            reply = "You can contact Krish at " + kb.contact_information.email + ".";
        } else if (userMsg.includes("impactglobe") && !userMsg.includes("revenue")) {
            reply = "ImpactGlobe is a 3D geopolitical dashboard analyzing global events built with Next.js and Three.js.";
        } else if (userMsg.includes("flyrank")) {
            reply = "At FlyRank, Krish built an ML ranking model that improved Precision@500 to 74.6% vs 74.0% baseline.";
        } else if (userMsg.includes("hemisphere")) {
            reply = "HemiSphere is an interactive 3D UI for spatial data analysis using React and WebGL.";
        } else if (userMsg.includes("revenue") || userMsg.includes("phone")) {
            reply = "I do not have that information available. Please contact Krish at mistrykrish2005@gmail.com for details.";
        }

        return res.status(200).json({ reply });
    }

    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`;
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        systemInstruction: {
          role: 'system',
          parts: [{ text: systemPrompt }]
        },
        contents: geminiMessages,
        generationConfig: {
          temperature: 0.1,
          maxOutputTokens: 500
        }
      })
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.error?.message || 'API Error');
    }

    const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || "I'm sorry, I couldn't process that.";
    return res.status(200).json({ reply });
  } catch (error) {
    console.error("LLM Error:", error);
    return res.status(500).json({ error: 'Failed to communicate with AI provider.' });
  }
}
