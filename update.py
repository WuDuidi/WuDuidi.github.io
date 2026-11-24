from pathlib import Path
import json
p=Path(__file__).parent
rows='''Empowering natural human–robot collaboration through multimodal language models and spatial intelligence: Pathways and perspectives|D Wu, P Zheng, Q Zhao, S Zhang, J Qi, J Hu, GN Zhu, L Wang|Robotics and Computer-Integrated Manufacturing 97, 103064|2026
H2R Bridge: Transferring vision-language models to few-shot intention meta-perception in human robot collaboration|D Wu, Q Zhao, J Fan, J Qi, P Zheng, J Hu|Journal of Manufacturing Systems 80, 524–535|2025
Computer vision-based intelligent elevator information system for efficient demand-based operation and optimization|D Wu, S Wu, Q Zhao, S Zhang, J Qi, J Hu, B Lin|Journal of Building Engineering 81, 108126|2024
A mixed reality-assisted human-to-robot skill transfer approach for contact-rich assembly via visuomotor primitives|D Wu, Q Zhao, Y Shen, J Li, P Zheng, J Qi, J Hu|Robotics and Computer-Integrated Manufacturing 99, 103208|2026
Overview of deep learning based pedestrian attribute recognition and re-identification|D Wu, H Huang, Q Zhao, S Zhang, J Qi, J Hu|Heliyon 8(12)|2022
Fall-related gait pattern recognition based on surface electromyography using a hybrid neural network with transfer learning|S Zhang, J Qi, S Hao, D Wu, Q Zhao, B Chen, J Hu|Biomedical Signal Processing and Control 98, 106771|2024
Generalized cross-domain framework for gesture recognition via wrist-worn sensing|S Zhang, J Qi, D Wu, Q Zhao, J Hu|IEEE Journal of Biomedical and Health Informatics 29(2), 996–1008|2024
E-GCDT: advanced reinforcement learning with GAN-enhanced data for continuous excavation system|Q Zhao, L Gao, D Wu, Y Lei, L Wang, J Qi, J Hu|Applied Intelligence 55(6), 413|2025
E-gtn: Advanced terrain sensing framework for enhancing intelligent decision making of excavators|Q Zhao, L Gao, D Wu, X Meng, J Qi, J Hu|Applied Sciences 14(16), 6974|2024
Coordination optimization control of DC component and harmonics for grid-connected PV inverters|B Long, C Zhao, D Wu, WT Fang, Y Lu, KT Chong|ISA Transactions 99, 432–444|2020
HAIL: Human-in-the-loop Assembly Imitation Learning System|Q Zhao, D Wu, Y Shen, J Li, Q Yu, S Zhang, J Qi, J Hu|Journal of Manufacturing Systems 86, 991–1006|2026
Cross-Domain Gesture Recognition via Wrist-Worn Sensing for Resource-Efficient IoT Applications|S Zhang, Y Ding, J Qi, C Hong, W Liu, D Wu, Q Zhao, J Hu|IEEE Internet of Things Journal|2025
Hybrid Consistency Policy: Decoupling Multi-Modal Diversity and Real-Time Efficiency in Robotic Manipulation|Q Zhao, Y Shen, X Zhai, D Wu, J Qi, C Hao, J Hu, Q Yu|IEEE Robotics and Automation Letters|2026
Real-time speed monitoring of elevator system based on low-cost IMU|S Zhang, C Hong, H Huang, D Wu, Q Zhao, J Qi, J Hu, Y Peng|IEEE Sensors Journal 23(15), 17559–17571|2023
DC component minimization of transformerless LCL-type grid-connected inverter with virtual capacitors|W Fang, D Wu, LJ Huang, B Long, Y Chen|Chinese Control Conference (CCC), 6520–6524|2019
Efficient multi-label attribute classification and recognition of microbiological bacteria based on deep learning and model fine-tuning|D Wu, H Huang, S Zhang, J Qi, D Wang, J Hu|bioRxiv, 2022.10.05.511056|2022
AssemBrain: Towards embodied intelligence paradigms for human-robot collaboration in manufacturing|D Wu, Q Zhao, S Zhang, J Qi, J Ma, GN Zhu, J Hu|Computers & Industrial Engineering, 112070|2026
Data augmentation for continuous excavation trajectories based on DGAN|Q Zhao, D Wu, S Zhang, J Qi, J Hu, GN Zhu|IEEE International Conference on Mechatronics and Automation (ICMA)|2024
RBF-NN based upper-bound adaptive learning sliding mode control for grid-connected converter|D Wu, B Long, Y Cheng|IEEE International Conference on Mechatronics and Automation (ICMA)|2020
Improving Intent Recognition with Multimodal Supervision for Human-Robot Interaction|D Wu, J Qi, Q Zhao, S Zhang, J Hu|International Conference on Automation in Manufacturing, Transportation and Logistics|2024
Deep learning-based abnormal elevator action detection system|Q Zhao, Y Chen, D Wu, Q Fan, H Huang, S Zhang, J Oi, J Hu|China Automation Congress (CAC), 1629–1634|2023
PAAM: Phase-Aware Action Modulation for Force-Guided Policy Augmentation in Contact-Rich Manipulation|Y Shen, Q Zhao, J Li, D Wu, J Hu, J Qi, C Hong, J Ma, R Du|IEEE International Conference on Mechatronics and Automation (ICMA)|2026
Lightweight Gated Residual Late Fusion for Frozen Vision Priors in Vision-Only Diffusion Policies|J Li, Q Zhao, D Wu, Y Shen, X Xu, H Xiong, S Shi, J Li, J Qi, J Hu|IEEE International Conference on Mechatronics and Automation (ICMA)|2026
A vision-language conditioned physics-aware imitation learning approach for bimanual robotic dexterous assembly|T Wang, B Gao, H Ma, G Zhang, D Wu, P Zheng|CIRP Annals|2026
Generative AI-Driven Pathways for Robot Skill Learning and Human-Guided Transfer for Smart Assembly|D Wu, P Zheng, Q Zhao, J Qi, J Hu|Procedia CIRP 147, 85–90 · Best Student Paper Award, CIRP CATS|2026
Fall-Related Gait Recognition Using Surface Electromyography with Transfer Learning|S Zhang, B Chen, D Wu, Q Zhao, C Hong, J Qi, J Hu|China Automation Congress (CAC), 290–295|2024
Towards Physical Intelligence in Contact-Rich Manufacturing: A Visual–Force–Pose Demonstration and Phase-Aware Learning Framework|Y Wang, R Zhang, MY Li, H Shi, J Wang, H Huang, D Wu, H Fang, et al.|SSRN 7525395 · Preprint|'''
old=json.loads((p/'publications.json').read_text(encoding='utf8'))
papers=[]
for row in rows.splitlines():
 title,authors,venue,year=row.split('|')
 match=next((x for x in old if x[0].lower()[:32]==title.lower()[:32]),None)
 papers.append([title,authors.replace('D Wu','Duidi Wu'),venue+(' · '+year if year else ''),*(match[3:] if match else ['','',''])])
# Preserve research emphasis, then list remaining work by year.
featured=['A mixed reality','Empowering','AssemBrain','H2R Bridge','Generative AI']
papers.sort(key=lambda x:next((i for i,s in enumerate(featured) if x[0].startswith(s)),5))
(p/'scholar-publications.json').write_text(json.dumps(papers,ensure_ascii=False,indent=2),encoding='utf8')
s=(p/'build.py').read_text(encoding='utf8')
s=s.replace('cards=[]',"papers=json.loads((p/'scholar-publications.json').read_text(encoding='utf8'))\ncards=[]")
s=s.replace('Publications documented in my CV. My name is highlighted in bold.','Journal articles, conference papers and preprints from my Google Scholar list. My name is highlighted in bold.')
(p/'build.py').write_text(s,encoding='utf8')
