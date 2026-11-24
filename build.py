from pathlib import Path
import html,json,urllib.parse
p=Path(__file__).parent
papers=[
('A mixed reality-assisted human-to-robot skill transfer approach for contact-rich assembly via visuomotor primitives','Duidi Wu, Qianyou Zhao, Yuliang Shen, Junlai Li, Pai Zheng, Jin Qi, Jie Hu','Robotics and Computer-Integrated Manufacturing 99, 103208 · 2026','A mixed reality','https://doi.org/10.1016/j.rcim.2025.103208','https://h2r-mrsta.github.io/'),
('Empowering natural human–robot collaboration through multimodal language models and spatial intelligence: Pathways and perspectives','Duidi Wu, Pai Zheng, Qianyou Zhao, et al.','Robotics and Computer-Integrated Manufacturing 97, 103064 · 2026','Empowering','',''),
('AssemBrain: Towards Embodied Intelligence Paradigms for Human-Robot Collaboration in Manufacturing','Duidi Wu, Qianyou Zhao, Shuo Zhang, et al.','Computers & Industrial Engineering 217, 112070 · 2026','AssemBrain','',''),
('H2R Bridge: Transferring vision-language models to few-shot intention meta-perception in human robot collaboration','Duidi Wu, Qianyou Zhao, Junming Fan, Jin Qi, Pai Zheng, Jie Hu','Journal of Manufacturing Systems 80, 524–535 · 2025','H2R Bridge','https://doi.org/10.1016/j.jmsy.2025.03.016',''),
('Generative AI-Driven Pathways for Robot Skill Learning and Human-Guided Transfer for Smart Assembly','Duidi Wu, Pai Zheng, Qianyou Zhao, Jin Qi, Jie Hu','Procedia CIRP 147, 85–90 · 2026 · Best Student Paper Award, CIRP CATS','Generative AI','https://doi.org/10.1016/j.procir.2026.02.122',''),
('Computer vision-based intelligent elevator information system for efficient demand-based operation and optimization','Duidi Wu, S. Wu, Qianyou Zhao, et al.','Journal of Building Engineering 81, 108126 · 2024','','',''),
('Overview of deep learning based pedestrian attribute recognition and re-identification','Duidi Wu, H. Huang, Qianyou Zhao, et al.','Heliyon 8(12), e12086 · 2022','','',''),
('HAIL: Human-in-the-loop Assembly Imitation Learning System','Qianyou Zhao, Duidi Wu, Yuliang Shen, et al.','Journal of Manufacturing Systems 86, 991–1006 · 2026','','',''),
('E-GCDT: advanced reinforcement learning with GAN-enhanced data for continuous excavation system','Qianyou Zhao, Le Gao, Duidi Wu, et al.','Applied Intelligence 55, 413 · 2025','','',''),
('Generalized cross-domain framework for gesture recognition via wrist-worn sensing','Shuo Zhang, Jin Qi, Duidi Wu, et al.','IEEE Journal of Biomedical and Health Informatics 29(2), 996–1008 · 2025','','',''),
('Improving Intent Recognition with Multimodal Supervision for Human-Robot Interaction','Duidi Wu, Jin Qi, Qianyou Zhao, et al.','ICaMaL · 2024','','https://doi.org/10.1109/ICaMaL62577.2024.10919851',''),
('Efficient Multi-Label Attribute Classification and Recognition of Bacteria Based on Deep Learning and model fine-tuning','Duidi Wu, H. Huang, Shuo Zhang, et al.','APCMBE & BME · 2023 · Youth Excellent Paper','','https://doi.org/10.1101/2022.10.05.511056',''),
('Data Augmentation for Continuous Excavation Trajectories Based on DGAN','Qianyou Zhao, Duidi Wu, Shuo Zhang, et al.','IEEE ICMA · 2024','','https://doi.org/10.1109/ICMA61710.2024.10633010',''),
('Fall-Related Gait Recognition Using Surface Electromyography with Transfer Learning','Shuo Zhang, B. Chen, Duidi Wu, et al.','China Automation Congress · 2024','','https://doi.org/10.1109/CAC63892.2024.10865421',''),
('Deep Learning-Based Abnormal Elevator Action Detection System','Qianyou Zhao, Y. Chen, Duidi Wu, et al.','China Automation Congress · 2023','','https://doi.org/10.1109/CAC59555.2023.10451419','')]
papers=json.loads((p/'scholar-publications.json').read_text(encoding='utf8'))
import re
def category(paper):
 venue=paper[2].lower()
 if 'biorxiv' in venue or 'ssrn' in venue:return 2
 if any(word in venue for word in ['conference','congress','procedia cirp']):return 1
 return 0
def author_rank(paper):
 names=[name.strip() for name in paper[1].split(',')]
 position=names.index('Duidi Wu')
 return min(position,2)
def year(paper):
 years=re.findall(r'\b(?:19|20)\d{2}\b',paper[2])
 return int(years[-1]) if years else 0
papers.sort(key=lambda paper:(category(paper),author_rank(paper),-year(paper)))
cards=[]
previous_category=None
for i,(title,authors,venue,prefix,url,project) in enumerate(papers):
 group=category(papers[i])
 if group!=previous_category:
  cards.append('<h3 class="publication-group">'+['Journal Articles','Conference Papers','Preprints'][group]+'</h3>')
  previous_category=group
 image=next((x for x in sorted((p/'images').iterdir()) if prefix and x.name.startswith(prefix)),None)
 visual=f'<img loading="lazy" src="{html.escape("images/"+image.name)}" alt="Graphical overview of {html.escape(title)}">' if image else '<div class="missing">'+('ROBOT LEARNING' if i<5 else 'RESEARCH')+'<small>Graphical abstract forthcoming</small></div>'
 link=url or 'https://scholar.google.com/scholar?q='+urllib.parse.quote(title)
 cards.append(f'<article class="paper">{visual}<div><h3>{html.escape(title)}</h3><p>{html.escape(authors).replace("Duidi Wu","<strong>Duidi Wu</strong>")}</p><p class="venue">{html.escape(venue)}</p><a href="{link}">Paper ↗</a>'+ (f' <a href="{project}">Webpage ↗</a>' if project else '')+'</div></article>')
(p/'publications.json').write_text(json.dumps(papers,ensure_ascii=False,indent=2),encoding='utf8')
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Duidi Wu | Robotics & Embodied Intelligence</title><meta name="description" content="Duidi Wu — robot skill learning, embodied intelligence and human–robot collaboration."><link rel="stylesheet" href="style.css"></head><body><a class="skip" href="#about">Skip to content</a><div class="layout"><aside><img class="portrait" src="images/wuduidi.jpeg" alt="Duidi Wu"><h1>Duidi Wu <span>武对娣</span></h1><p class="role">Robotics & Embodied Intelligence</p><p>Postdoctoral Fellow<br>The Hong Kong Polytechnic University</p><p class="muted">August 2026–present</p><a href="mailto:wu_duidi@sjtu.edu.cn">wu_duidi@sjtu.edu.cn</a><div class="social"><a href="https://scholar.google.com.hk/citations?user=6MDg18IAAAAJ&hl=en">Google Scholar ↗</a></div><nav><a href="#about">About</a><a href="#news">News & Highlights</a><a href="#publications">Publications</a><a href="#service">Reviewer Service</a></nav></aside><main><section id="about"><h2>About Me</h2><p>I am a Postdoctoral Fellow at <a href="https://www.polyu.edu.hk/">The Hong Kong Polytechnic University</a>, where I have been working since August 2026.</p><p>I received my Ph.D. in Mechanical Engineering from <a href="https://en.sjtu.edu.cn/">Shanghai Jiao Tong University</a> in 2026, supervised by Jin Qi and Jie Hu. During my Ph.D., I participated in the Joint PhD Supervision Scheme at The Hong Kong Polytechnic University from August 2025 to May 2026, working with Pai Zheng. Before that, I received my B.Eng. in Mechanical Design, Manufacturing and Automation from the <a href="https://en.uestc.edu.cn/">University of Electronic Science and Technology of China</a> in 2021.</p><p>My research focuses on <strong>robot skill learning, embodied intelligence, and human–robot collaboration</strong>, with particular interests in imitation learning, mixed reality-assisted skill transfer, aerial manipulation, and intelligent manufacturing. My doctoral work explored robot assembly skill learning and transfer for human–robot collaboration.</p></section><section id="news"><div class="section-title"><h2>News & Highlights</h2><span>Selected milestones</span></div><ul class="news"><li><time>Apr 2026</time><div><b>Best Student Paper Award</b> at CIRP CATS 2026, Hong Kong.</div></li><li><time>Dec 2025</time><div><b>National Scholarship for Doctoral Students</b> (top 3%) and Shanghai Outstanding Graduate recognition.</div></li><li><time>Nov 2025</time><div><b>Best Presentation & Best Poster Awards</b> at the 3rd Human-Centric Intelligent Manufacturing Conference, Beijing.</div></li><li><time>Aug 2025</time><div>Joined the Joint PhD Supervision Scheme at The Hong Kong Polytechnic University.</div></li></ul></section><section id="publications"><div class="section-title"><h2>Publications</h2></div>CARDS</section><section id="service"><h2>Reviewer Service</h2><p>I have served as a reviewer for the following journals:</p><h3 class="service-heading">CAS Tier 1</h3><ul class="reviewers"><li>Robotics and Computer-Integrated Manufacturing (RCIM)</li><li>Information Fusion (Inf. Fusion)</li><li>Artificial Intelligence Review (Artif. Intell. Rev.)</li></ul><h3 class="service-heading">CAS Tier 2</h3><ul class="reviewers"><li>Neural Networks (Neural Netw.)</li><li>IEEE Robotics and Automation Letters (RA-L)</li><li>Robotics and Autonomous Systems (RAS)</li></ul><h3 class="service-heading">Other Journals</h3><ul class="reviewers"><li>Journal of Intelligent &amp; Robotic Systems (J. Intell. Robot. Syst.)</li><li>Frontiers in Robotics and AI (Front. Robot. AI)</li><li>Sustainable Futures (Sustain. Futures)</li><li>Research in Engineering Design (Res. Eng. Des.)</li><li>Cognitive Computation (Cogn. Comput.)</li><li>Scientific Reports (Sci. Rep.)</li></ul></section><footer>© Duidi Wu · <a href="mailto:wu_duidi@sjtu.edu.cn">Get in touch</a></footer></main></div></body></html>'''
(p/'index.html').write_text(page.replace('CARDS',''.join(cards)),encoding='utf8')
