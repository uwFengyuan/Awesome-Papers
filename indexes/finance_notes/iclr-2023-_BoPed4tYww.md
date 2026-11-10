# Timing is Everything: Learning to Act Selectively with Costly Actions and Budgetary Constraints

ICLR 2023 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Many real-world settings involve costs for performing actions; transaction costsin financial systems and fuel costs being common examples. / We show LICRA learns theoptimal value function and ensures budget constraints are satisfied almost surely.We demonstrate empirically LICRA’s superior performance against benchmarkRL methods in OpenAI gym’s Lunar Lander and in Highway environments and avariant of the Merton portfolio problem within finance.

[Paper](https://openreview.net/forum?id=_BoPed4tYww)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Investment Evaluation & Decisions / 投资评价与决策 → General / 综合

## Abstract / 摘要

Many real-world settings involve costs for performing actions; transaction costsin financial systems and fuel costs being common examples. In these settings,performing actions at each time step quickly accumulates costs leading to vastlysuboptimal outcomes. Additionally, repeatedly acting produces wear and tear andultimately, damage. Determining when to act is crucial for achieving successfuloutcomes and yet, the challenge of efficiently learning to behave optimally whenactions incur minimally bounded costs remains unresolved. In this paper, we intro-duce a reinforcement learning (RL) framework named Learnable Impulse ControlReinforcement Algorithm (LICRA), for learning to optimally select both whento act and which actions to take when actions incur costs. At the core of LICRAis a nested structure that combines RL and a form of policy known as impulsecontrol which learns to maximise objectives when actions incur costs. We provethat LICRA, which seamlessly adopts any RL method, converges to policies thatoptimally select when to perform actions and their optimal magnitudes. We thenaugment LICRA to handle problems in which the agent can perform at most k < ∞actions and more generally, faces a budget constraint. We show LICRA learns theoptimal value function and ensures budget constraints are satisfied almost surely.We demonstrate empirically LICRA’s superior performance against benchmarkRL methods in OpenAI gym’s Lunar Lander and in Highway environments and avariant of the Merton portfolio problem within finance.
