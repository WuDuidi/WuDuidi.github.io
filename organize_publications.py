from pathlib import Path
import json
p=Path(__file__).parent
data=json.loads((p/'scholar-publications.json').read_text(encoding='utf8'))
webpages={'Empowering':'https://github.com/WuDuidi/MLLM-HRC-Survey','AssemBrain':'https://assembrain.github.io/','E-GCDT':'https://zqy-an.github.io/ExcavatorRL.github.io/','HAIL:':'https://hailzqy.github.io/HAIL.github.io/'}
for paper in data:
 for prefix,url in webpages.items():
  if paper[0].startswith(prefix):paper[5]=url
(p/'scholar-publications.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
s=(p/'build.py').read_text(encoding='utf8')
s=s.replace('cards=[]', '''import re
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
 years=re.findall(r'\\b(?:19|20)\\d{2}\\b',paper[2])
 return int(years[-1]) if years else 0
papers.sort(key=lambda paper:(category(paper),author_rank(paper),-year(paper)))
cards=[]
previous_category=None''')
s=s.replace(' image=next(',''' group=category(papers[i])
 if group!=previous_category:
  cards.append('<h3 class="publication-group">'+['Journal Articles','Conference Papers','Preprints'][group]+'</h3>')
  previous_category=group
 image=next(''')
s=s.replace('{"Paper ↗" if url else "Find paper ↗"}','Paper ↗').replace('Project ↗','Webpage ↗')
s=s.replace('My name is highlighted in bold.','Within each section: first-author papers, then second-author papers, followed by other co-authored work; newest first within each group. My name is highlighted in bold.')
(p/'build.py').write_text(s,encoding='utf8')
with (p/'style.css').open('a',encoding='utf8') as f:f.write('\n.publication-group{font-size:21px;margin:32px 0 4px;padding-bottom:10px;border-bottom:2px solid #222}\n')
