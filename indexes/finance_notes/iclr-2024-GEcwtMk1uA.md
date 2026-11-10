# Identifying the Risks of LM Agents with an LM-Emulated Sandbox

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：(e.g., GPT-4) Agent Action - emu. tool exec. & states Send the annual financial report to Alice … - adv. emu. for red-teaming Evaluator

[Paper](https://openreview.net/forum?id=GEcwtMk1uA)

Classification / 分类：Financial Safety & Compliance / 金融安全与合规 → Financial Privacy & Security / 金融隐私与信息安全 → General / 综合

## Abstract / 摘要

Recent advances in Language Model (LM) agents and tool use, exemplified by applications like ChatGPT Plugins, enable a rich set of capabilities but also amplify potential risks—such as leaking private data or causing financial losses. Identifying these risks is labor-intensive, necessitating implementing the tools, setting up the environment for each test scenario manually, and finding risky cases. As tools and agents become more complex, the high cost of testing these agents will make it increasingly difficult to find high-stakes, long-tail risks. To address these challenges, we introduce ToolEmu: a framework that uses an LM to emulate tool execution and enables scalable testing of LM agents against a diverse range of tools and scenarios. Alongside the emulator, we develop an LM-based automatic safety evaluator that examines agent failures and quantifies associated risks. We test both the tool emulator and evaluator through human evaluation and find that 68.8% of failures identified with ToolEmu would be valid real-world agent failures. Using our curated initial benchmark consisting of 36 high-stakes toolkits and 144 test cases, we provide a quantitative risk analysis of current LM agents and identify numerous failures with potentially severe outcomes. Notably, even the safest LM agent exhibits such failures 23.9% of the time according to our evaluator, underscoring the need to develop safer LM agents for real-world deployment.
