# Computer Use at the Edge of the Statistical Precipice

NeurIPS 2026 · main · Long

[Long] [Main] [Oral] [Finance]

Financial evidence / 金融依据：erarchical structure plugs directly into the evaluation methodology of Section 4. Fifteen apps across seven domains. The 15 applications span 7 real-world domains (Table 4, Appendix E): communication (Email, Messaging), financial services (Payment, Banking), shopping (E-Commerce, QwikShop, Auction), entertainment (Music, Video), on-demand services (Eats, Ryde), travel (Flight Booking, Transit), and smart living (Smart Home, Parking). Each application is a fully-featured React Native Android application, 6

[Paper](https://openreview.net/forum?id=We2oXEmu4W)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Banking Dialogue & Intent / 银行对话与意图 → General / 综合

## Abstract / 摘要

Evaluating Computer Use Agents (CUAs) on interactive environments is fraught with methodological pitfalls that the field has yet to systematically address. We show that a 1MB replay script that blindly executes a recorded action sequence without ever observing the screen outperforms frontier models on prominent static benchmarks, and prove that its expected success rate is exactly equal to the source agent's pass@k in deterministic environments. We trace this and other failures to two root causes: non-principled environment design (static, unsandboxed, or unreliably verified environments) and non-principled evaluation methodology (naïve aggregation and misuse of pass@k for stateful UI interactions). To address the first, we propose PRISM, five design principles for CUA environments (privileged verification, realistic environments, integrity-checked configurations, sandboxed execution, and multifactorial variability) and instantiate them in DigiWorld, a benchmark of 15 realistic sandboxed mobile applications able to evaluate agents in over 3.2 million verified unique configurations. To address the second, we develop an aggregation framework pairing Wilson score intervals with hierarchical bootstrap, producing confidence intervals that correctly account for the nested structure of CUA benchmarks, as we empirically demonstrate. All together, we show that principled environment design and rigorous evaluation methodology are not optional refinements but prerequisites for meaningful CUA research.
