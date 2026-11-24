from pathlib import Path
import re
p=Path(__file__).parent
s=(p/'build.py').read_text(encoding='utf8')
s=s.replace('<a href="#education">Education</a>','')
s=s.replace('Mechanical Engineering<br>Shanghai Jiao Tong University','Postdoctoral Fellow<br>The Hong Kong Polytechnic University')
s=s.replace('Ph.D. research, 2021–2026<br>Joint Ph.D. supervision, PolyU<br>2025–2026','August 2026–present')
about='''<section id="about"><h2>About Me</h2><p>I am a Postdoctoral Fellow at <a href="https://www.polyu.edu.hk/">The Hong Kong Polytechnic University</a>, where I have been working since August 2026.</p><p>I received my Ph.D. in Mechanical Engineering from <a href="https://en.sjtu.edu.cn/">Shanghai Jiao Tong University</a> in 2026, supervised by Jin Qi and Jie Hu. During my Ph.D., I participated in the Joint PhD Supervision Scheme at The Hong Kong Polytechnic University from August 2025 to May 2026, working with Pai Zheng. Before that, I received my B.Eng. in Mechanical Design, Manufacturing and Automation from the <a href="https://en.uestc.edu.cn/">University of Electronic Science and Technology of China</a> in 2021.</p><p>My research focuses on <strong>robot skill learning, embodied intelligence, and human–robot collaboration</strong>, with particular interests in imitation learning, mixed reality-assisted skill transfer, aerial manipulation, and intelligent manufacturing. My doctoral work explored robot assembly skill learning and transfer for human–robot collaboration.</p></section>'''
s=re.sub(r'<section id="about">.*?</section>',lambda m:about,s)
s=re.sub(r'<section id="education">.*?</section>','',s)
groups=[('CAS Tier 1',['Robotics and Computer-Integrated Manufacturing','Information Fusion','Artificial Intelligence Review']),('CAS Tier 2',['Neural Networks','IEEE Robotics and Automation Letters (RA-L)','Robotics and Autonomous Systems (RAS)']),('Other Journals',['Journal of Intelligent &amp; Robotic Systems','Frontiers in Robotics and AI','Sustainable Futures','Research in Engineering Design','Cognitive Computation','Scientific Reports'])]
service='<section id="service"><h2>Reviewer Service</h2><p>I have served as a reviewer for the following journals:</p>'
for name,journals in groups:
 service+='<h3 class="service-heading">'+name+'</h3><ul class="reviewers">'+''.join('<li>'+j+'</li>' for j in journals)+'</ul>'
service+='</section>'
s=re.sub(r'<section id="service">.*?</section>',lambda m:service,s)
(p/'build.py').write_text(s,encoding='utf8')
with (p/'style.css').open('a',encoding='utf8') as f:
 f.write('\n#about h2{font-family:inherit;font-size:28px;font-weight:600;line-height:1.3;margin:0 0 24px}#about p{line-height:1.85;margin:0 0 20px}#about a{text-decoration:underline;text-underline-offset:3px}.service-heading{font-size:16px;margin:24px 0 10px}.reviewers{margin-top:0}\n')
