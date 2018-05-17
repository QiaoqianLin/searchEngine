import os
import sys
import codecs
from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup
# es_index_data
dict = {
    '5-year-bs-ms-program':'https://cs.illinois.edu/academics/graduate/fifth-year-masters-programs/5-year-bs-ms-program',
    '5-year-bs-mcs-program':'https://cs.illinois.edu/academics/graduate/fifth-year-masters-programs/5-year-bs-mcs-program',
    'bs-computer-science-engineering':'https://cs.illinois.edu/academics/degree-program-options/bs-computer-science-engineering',
    'bs-mathematics-computer-science':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/bs-mathematics-computer-science',
    'bs-statistics-computer-science':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/bs-statistics-computer-science',
    'computer-science-anthropology':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/cs-x-degree-programs/computer-science-anthropology',
    'computer-science-astronomy':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/cs-x-degree-programs/computer-science-astronomy',
    'computer-science-chemistry':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/cs-x-degree-programs/computer-science-chemistry',
    'computer-science-crop-sciences':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/cs-x-degree-programs/computer-science-crop-sciences',
    'computer-science-linguistics':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/cs-x-degree-programs/computer-science-linguistics',
    'computer-science-music':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/cs-x-degree-programs/computer-science-music',
    'cpt-training-process':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/international-students/cpt-training-process',
    'cs-course-restrictions-enrollment-caps':'https://cs.illinois.edu/academics/undergraduate/registration/cs-course-restrictions-enrollment-caps',
    'cs-x-degree-programs':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/cs-x-degree-programs',
    'cs-x-faq':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/cs-x-degree-programs/cs-x-faq',
    'degree-program-options':'https://cs.illinois.edu/academics/degree-program-options',
    'epi-exam-requirements':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/international-students/epi-exam-requirements',
    'explore-courses':'https://cs.illinois.edu/academics/courses',
    'fifth-year-masters-programs':'https://cs.illinois.edu/academics/graduate/fifth-year-masters-programs',
    'final-exam-thesis-defense':'https://cs.illinois.edu/academics/graduate/phd-program/final-exam-thesis-defense',
    'graduate-advising-contacts':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/graduate-advising-contacts',
    'graduate-forms-advising-resources':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources',
    'graduate-student-annual-evaluation-process':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/graduate-student-annual-evaluation-process',
    'graduate':'https://cs.illinois.edu/academics/graduate',
    'guidelines-forming-phd-committee':'https://cs.illinois.edu/academics/graduate/phd-program/guidelines-forming-phd-committee',
    'honor-code':'https://cs.illinois.edu/academics/honor-code',
    'honors':'https://cs.illinois.edu/academics/undergraduate/honors',
    'mcs-campus':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/new-graduate-student-resources/mcs-campus',
    'mcs-data-science-track-requirements':'https://cs.illinois.edu/academics/graduate/professional-mcs-program/mcs-data-science-track-requirements',
    'mcs-data-science-track':'https://cs.illinois.edu/academics/graduate/professional-mcs-program/mcs-data-science-track',
    'mcs-degree-requirements':'https://cs.illinois.edu/academics/graduate/professional-mcs-program/mcs-degree-requirements',
    'minor-computer-science':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/minor-computer-science',
    'ms-bioinformatics-program':'https://cs.illinois.edu/academics/graduate/ms-bioinformatics-program',
    'ms-general':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/new-graduate-student-resources/ms-general',
    'ms-program':'https://cs.illinois.edu/academics/graduate/ms-program',
    'new-graduate-student-resources':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/new-graduate-student-resources',
    'non-degree-options':'https://cs.illinois.edu/academics/graduate/non-degree-options',
    'official-forms':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/official-forms',
    'online-mcs-degree-requirements':'https://cs.illinois.edu/academics/graduate/professional-mcs-program/online-mcs/online-mcs-degree-requirements',
    'online-mcs':'https://cs.illinois.edu/academics/graduate/professional-mcs-program/online-mcs',
    'opt-training-process':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/international-students/opt-training-process',
    'phd-general':'https://cs.illinois.edu/academics/graduate/graduate-forms-advising-resources/new-graduate-student-resources/phd-general',
    'phd-ms-thesis-format-review-guidelines':'https://cs.illinois.edu/academics/graduate/phd-program/phd-ms-thesis-format-review-guidelines',
    'phd-program-study-process':'https://cs.illinois.edu/academics/graduate/phd-program/phd-program-study-process',
    'phd-program':'https://cs.illinois.edu/academics/graduate/phd-program',
    'phd-requirements':'https://cs.illinois.edu/academics/graduate/phd-program/phd-requirements',
    'phd-time-limits-milestones':'https://cs.illinois.edu/academics/graduate/phd-program/phd-time-limits-milestones',
    'policies-and-procedures':'https://cs.illinois.edu/academics/undergraduate/policies-and-procedures',
    'preliminary-exam':'https://cs.illinois.edu/academics/graduate/phd-program/preliminary-exam',
    'professional-mcs-program':'https://cs.illinois.edu/academics/graduate/professional-mcs-program',
    'qualifying-exam':'https://cs.illinois.edu/academics/graduate/phd-program/qualifying-exam',
    'registration':'https://cs.illinois.edu/academics/undergraduate/registration',
    'science-electives-cs':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/bs-computer-science-engineering/science-electives-cs',
    'software-engineering-certificate':'https://cs.illinois.edu/academics/undergraduate/degree-program-options/software-engineering-certificate',
    'student-resources':'https://cs.illinois.edu/academics/student-life/student-resources',
    'undergraduate-advising':'https://cs.illinois.edu/academics/undergraduate/undergraduate-advising',
    'undergraduate-forms':'https://cs.illinois.edu/academics/undergraduate/undergraduate-forms',
    'undergraduate':'https://cs.illinois.edu/admissions/undergraduate',
    'application-checklist':'https://cs.illinois.edu/admissions/graduate/application-checklist',
    'application-deadlines':'https://cs.illinois.edu/admissions/graduate/application-deadlines',
    'application-process-current-cs-illinois':'https://cs.illinois.edu/admissions/graduate/applications-process-requirements/application-process-current-cs-illinois',
    'applications-process-requirements':'https://cs.illinois.edu/admissions/graduate/applications-process-requirements',
    'degree-program-options':'https://cs.illinois.edu/academics/degree-program-options',
    'faqs':'https://cs.illinois.edu/admissions/graduate/faqs',
    'financial-aid':'https://cs.illinois.edu/admissions/financial-aid',
    'graduate':'https://cs.illinois.edu/admissions/graduate',
    'online-mcs-faqs':'https://cs.illinois.edu/admissions/graduate/faqs/online-mcs-faqs',
    'transfer-students':'https://cs.illinois.edu/admissions/undergraduate/transfer-students',
    'undergraduate':'https://cs.illinois.edu/admissions/undergraduate',
    'why-cs-illinois':'https://cs.illinois.edu/admissions/why-cs-illinois',
    'architecture-compilers-and-parallel-computing':'https://cs.illinois.edu/research/architecture-compilers-and-parallel-computing',
    'artificial-intelligence':'https://cs.illinois.edu/research/artificial-intelligence',
    'bioinformatics-and-computational-biology':'https://cs.illinois.edu/research/bioinformatics-and-computational-biology',
    'computers-and-education':'https://cs.illinois.edu/research/computers-and-education',
    'corporate-partners':'https://cs.illinois.edu/research/corporate-partners',
    'database-and-information-systems':'https://cs.illinois.edu/research/database-and-information-systems',
    'graphics-visualization-and-hci':'https://cs.illinois.edu/research/graphics-visualization-and-hci',
    'information-network-academic-research-center':'https://cs.illinois.edu/research/database-and-information-systems/information-network-academic-research-center',
    'programming-languages-formal-methods-and-software-engineering':'https://cs.illinois.edu/research/programming-languages-formal-methods-and-software-engineering',
    'scientific-computing':'https://cs.illinois.edu/research/scientific-computing',
    'systems-and-networking':'https://cs.illinois.edu/research/systems-and-networking',
    'theory-and-algorithms':'https://cs.illinois.edu/research/theory-and-algorithms'
}

def process_text(text):
    text = text.strip().replace('\n', ' ')
    return ' '.join(text.split())

def index_data(folder):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])

    for filename in os.listdir(os.path.join(dir_path, 'data/'+folder)):
        if filename.endswith('.html'):
            # print(filename)
            file_path = os.path.join(dir_path, 'data/'+folder, filename)
            article_id = filename.replace('.html', '')
            # url = 'https://cs.illinois.edu/{0}/{1}'.format(folder,dict[article_id])
            url = dict[article_id]
            html_content = codecs.open(file_path, 'r', encoding='utf-8')
            soup = BeautifulSoup(html_content, 'lxml')
            # title = soup.find().text
            content = soup.find().text
            # print("title",title)
            # print("content",content)
            es.index(index='cs_index', doc_type='ariticle', id=article_id, body={
                'url': url,
                # 'title': process_text(title),
                'content': process_text(content)
            })