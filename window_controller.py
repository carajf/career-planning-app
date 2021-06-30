import sys
import webbrowser
import action_plan as ap
import skills as sk
import jobs as jb
import login as lg
import experience as exp
import education as ed
import welcome_screen as ws
import create_user as cu
import user_login as ul
import ui_main as um

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


# Class for calling user selection screen
class Welcome_Screen(QMainWindow, ws.Ui_WS_Main_Window):
    def __init__(self):
        super(Welcome_Screen, self).__init__()
        self.setupUi(self)

        # Make all the user frames invisible

        self.userframe_1.setHidden(True)
        self.userframe_2.setHidden(True)
        self.userframe_3.setHidden(True)
        self.userframe_4.setHidden(True)
        self.userframe_5.setHidden(True)
        self.userframe_6.setHidden(True)
        self.userframe_7.setHidden(True)
        self.userframe_8.setHidden(True)

        # Show only as many user frames as many users there are in the database
        # and display their names

        i = 0
        for u in lg.get_usr_list():
            if i == 0:
                self.placeholder_name_1.clear()
                self.userframe_1.setHidden(False)
                item = QtWidgets.QListWidgetItem()
                name = ''.join(u)
                item.setText(name)
                self.placeholder_name_1.addItem(item)
            if i == 1:
                self.placeholder_name_2.clear()
                self.userframe_2.setHidden(False)
                item = QtWidgets.QListWidgetItem()
                name = ''.join(u)
                item.setText(name)
                self.placeholder_name_2.addItem(item)
            if i == 2:
                self.placeholder_name_3.clear()
                self.userframe_3.setHidden(False)
                item = QtWidgets.QListWidgetItem()
                name = ''.join(u)
                item.setText(name)
                self.placeholder_name_3.addItem(item)
            if i == 3:
                self.placeholder_name_4.clear()
                self.userframe_4.setHidden(False)
                item = QtWidgets.QListWidgetItem()
                name = ''.join(u)
                item.setText(name)
                self.placeholder_name_4.addItem(item)
            if i == 4:
                self.placeholder_name_5.clear()
                self.userframe_5.setHidden(False)
                item = QtWidgets.QListWidgetItem()
                name = ''.join(u)
                item.setText(name)
                self.placeholder_name_5.addItem(item)
            if i == 5:
                self.placeholder_name_6.clear()
                self.userframe_6.setHidden(False)
                item = QtWidgets.QListWidgetItem()
                name = ''.join(u)
                item.setText(name)
                self.placeholder_name_6.addItem(item)
            if i == 6:
                self.placeholder_name_7.clear()
                self.userframe_7.setHidden(False)
                item = QtWidgets.QListWidgetItem()
                name = ''.join(u)
                item.setText(name)
                self.placeholder_name_7.addItem(item)
            if i == 7:
                self.placeholder_name_8.clear()
                self.userframe_8.setHidden(False)
                item = QtWidgets.QListWidgetItem()
                name = ''.join(u)
                item.setText(name)
                self.placeholder_name_8.addItem(item)
            i += 1

        # Make button clickable
        self.pushButton.clicked.connect(self.openRegisterWindow)
        self.pushButton.clicked.connect(self.close)

        # Make each user name clickable
        self.placeholder_name_1.itemClicked.connect(self.logUserIn)
        self.placeholder_name_2.itemClicked.connect(self.logUserIn)
        self.placeholder_name_3.itemClicked.connect(self.logUserIn)
        self.placeholder_name_4.itemClicked.connect(self.logUserIn)
        self.placeholder_name_5.itemClicked.connect(self.logUserIn)
        self.placeholder_name_6.itemClicked.connect(self.logUserIn)
        self.placeholder_name_7.itemClicked.connect(self.logUserIn)
        self.placeholder_name_8.itemClicked.connect(self.logUserIn)

    def logUserIn(self, item):
        self.username = item.text()
        self.window = User_Login_Screen(self.username)
        self.window.show()
        self.close()

    def openRegisterWindow(self):
        self.window = Register_Screen()
        self.window.show()

    def close_window(self):
        self.close()


# Class for calling register window
class Register_Screen(QMainWindow, cu.Ui_Login_Main_Window):
    def __init__(self):
        super(Register_Screen, self).__init__()
        self.setupUi(self)

        # Create a new user and go back to login screen
        self.btn_create_account.clicked.connect(self.addUser)

        # Go back to login screen
        self.btn_back_button.clicked.connect(self.go_back)
        self.btn_back_button.clicked.connect(self.close)

        # Hide error message until its used
        self.lbl_error_placeholder.setHidden(True)

    def addUser(self):
        firstname = self.edit_enter_password_2.text()
        email = self.edit_enter_password_4.text()
        password = self.edit_enter_password.text()
        password2 = self.edit_enter_password_3.text()
        if firstname != "" and email != "" and password != "":
            if password2 == password:
                lg.enter_new_user(firstname, email, password)
                self.go_back()
                self.close()
            else:
                self.lbl_error_placeholder.setHidden(False)
                self.lbl_error_placeholder.setText("Passwords have to match!")
        else:
            self.lbl_error_placeholder.setHidden(False)
            self.lbl_error_placeholder.setText("Name, email and password cannot be empty")

    def go_back(self):
        self.window = Welcome_Screen()
        self.window.show()


# Class for calling user login screen
class User_Login_Screen(QMainWindow, ul.Ui_Login_Main_Window):
    def __init__(self, username):
        super(User_Login_Screen, self).__init__()
        self.setupUi(self)
        self.username = username

        self.lbl_username.setText(self.username)

        self.btn_login.clicked.connect(self.login)

        self.btn_back_button.clicked.connect(self.go_back)
        self.btn_back_button.clicked.connect(self.close)

        self.lbl_error_placeholder.setHidden(True)

    def login(self):
        username = self.username
        password = self.edit_enter_password.text()
        if lg.login(username, password):
            self.lbl_error_placeholder.setStyleSheet("color: rgb(0, 255, 0);")
            self.lbl_error_placeholder.setText("Successful login!")
            self.lbl_error_placeholder.setHidden(False)
            self.window = Main_Screen(username)
            self.window.show()
            self.close()
        else:
            self.lbl_error_placeholder.setStyleSheet("color: rgb(255, 0, 0);")
            self.lbl_error_placeholder.setText("Wrong Password!")
            self.lbl_error_placeholder.setHidden(False)

    def go_back(self):
        self.window = Welcome_Screen()
        self.window.show()


class Main_Screen(QMainWindow, um.Ui_ui_main):

    def __init__(self, username):

        super(Main_Screen, self).__init__()
        self.setupUi(self)
        self.lbl_selected_item.setHidden(True)
        self.username = username
        self.menu_toggled = False
        self.menu_widget.setHidden(True)
        self.popup_hidden = True

        ap.userID = self.username
        jb.userID = self.username
        exp.userID = self.username
        ed.userID = self.username
        sk.userID = self.username
        sk.create_table()
        ed.create_table()
        exp.create_table()
        ap.create_table()
        jb.create_table()


        #################################
        # Functionalities for main menu #
        #################################

        self.ALL_STACKED_PAGES.setCurrentWidget(self.HOME_PAGE_MAIN)
        self.lbl_welcome_home.setText("Welcome to your home screen, "+self.username)

        # The main 4 buttons
        self.portfolio_frame_button.clicked.connect(self.open_portfolio)
        self.new_skills_frame_button.clicked.connect(self.open_skills)
        self.find_job_frame_button.clicked.connect(self.open_jobs)
        self.action_plan_frame_button.clicked.connect(self.open_plan)

        # The back button
        self.last_widget = self.ALL_STACKED_PAGES.currentWidget()
        self.btn_back_button.clicked.connect(self.open_home)

        # Show menu
        self.btn_toggle_menu.clicked.connect(self.toggle_menu)

        # Buttons in menu
        # Home
        self.home_button.clicked.connect(self.open_home)
        # Portfolio
        self.btn_intropsection.clicked.connect(self.open_portfolio)
        # Find a Job
        self.btn_find_a_job.clicked.connect(self.open_find_jobs)
        # Jobs Found
        self.btn_jobs_found_2.clicked.connect(self.open_jobs_found)
        # New Skills
        self.btn_new_skills.clicked.connect(self.open_skills)
        # Action Plan
        self.btn_action_plan.clicked.connect(self.open_plan)
        # Settings
        self.btn_my_account.clicked.connect(self.open_settings)
        # Quit
        self.btn_sign_out.clicked.connect(self.quit_app)


        ######################################
        # Functionalities for user portfolio #
        ######################################

        # Add skill buttons
        self.btn_new_item.clicked.connect(self.add_item)
        self.btn_skill.clicked.connect(self.add_skill)
        self.btn_education.clicked.connect(self.add_education)
        self.btn_work_exp.clicked.connect(self.add_experience)
        self.btn_add_skill.clicked.connect(self.add_to_skill_list)
        self.btn_save_skills.clicked.connect(self.send_skills)

        # Go to resources button
        self.btn_resources.clicked.connect(self.open_skills)

        # Make skills clickable
        self.skills_list.itemClicked.connect(self.skill_clicked)
        self.experience_list.itemClicked.connect(self.work_clicked)
        self.education_list.itemClicked.connect(self.edu_clicked)

        # Display skills
        self.edit_skill_dropdown.clear()
        self.skills_list.clear()

        for skill in sk.check_skills():
            s = ''.join(skill)
            self.edit_skill_dropdown.addItem(s)
            self.skills_list.addItem(s)

        # Skills to be added
        self.skills_to_add = []
        self.new_skills_list.clear()

        # Edit skill
        self.edit_skill_dropdown.activated.connect(self.skill_edit_clicked)

        # Edit education
        self.edit_education_dropdown.activated.connect(self.edu_edit_clicked)

        # Edit work exp
        self.edit_job_dropdown.activated.connect(self.job_edit_clicked)

        # Add education buttons
        self.btn_add_education.clicked.connect(self.add_to_edu_list)
        self.btn_save_education.clicked.connect(self.send_education)

        # Add education functionality
        self.edit_education_dropdown.clear()
        self.new_education_list.clear()
        self.education_list.clear()

        self.edu_to_add = []
        ed.userID = self.username

        # Display Education

        for edu in ed.check_edu():
            e = ''.join(edu)
            self.edit_education_dropdown.addItem(e)
            self.education_list.addItem(e)

        # Add work experience buttons

        self.btn_add_job.clicked.connect(self.add_to_work_list)
        self.btn_save_jobs.clicked.connect(self.send_work_exp)

        # Add work experience functionality

        self.edit_job_dropdown.clear()
        self.new_jobs_list.clear()
        self.experience_list.clear()

        self.work_to_add = []
        exp.userID = self.username

        # Display work experience

        for work in exp.check_work_exp():
            w = ''.join(work)
            self.edit_job_dropdown.addItem(w)
            self.experience_list.addItem(w)

        # Delete skills, edu and experience
        self.delete_skill.clicked.connect(self.delete_skill_clicked)
        self.delete_education.clicked.connect(self.delete_education_clicked)
        self.delete_work_experience.clicked.connect(self.delete_experience_clicked)

        self.popup_skill_deleted.setHidden(True)
        self.popup_education_deleted.setHidden(True)
        self.popup_experience_deleted.setHidden(True)

        ##################################
        # Functionalities for find a job #
        ##################################

        # The 2 main buttons
        self.btn_jobs_found.clicked.connect(self.jobs_found_clicked)
        self.btn_find_job.clicked.connect(self.find_a_job_clicked)

        # Add job button
        self.btn_new_job.clicked.connect(self.add_new_job_clicked)

        # Add and edit job main
        self.btn_save_job.clicked.connect(self.save_job)
        self.btn_save_job.clicked.connect(self.load_tables)
        self.delete_job.clicked.connect(self.delete_job_clicked)

        # Display job details
        self.jobs_found_table.itemClicked.connect(self.job_clicked)

        # Edit job
        self.edit_job_dropdown_2.clear()
        list_of_jobs = jb.check_jobs()
        for jobs in list_of_jobs:
            self.edit_job_dropdown_2.addItem(jobs[0])
        self.edit_job_dropdown_2.activated.connect(self.edit_job_clicked)

        # Find a job
        self.list_of_resources = [
            "https://elearningindustry.com/prepare-yourself-for-a-job-interview-6-top-online-resources",
            "https://www.prospects.ac.uk/careers-advice/interview-tips/how-to-prepare-for-an-interview",
            "https://www.careerbuilder.com/advice/topic/interviews",
            "https://www.prospects.ac.uk/careers-advice/applying-for-jobs/write-a-successful-job-application",
            "https://www.thebalancecareers.com/how-to-apply-for-jobs-online-2061598",
            "https://help.open.ac.uk/applying-for-jobs-an-overview-of-the-process"]

        self.list_resources_3.clear()
        for item in self.list_of_resources:
            self.list_resources_3.addItem(item)


        ###################################
        # Functionalities for Action Plan #
        ###################################
        self.btn_add_row.clicked.connect(self.save_tables)
        self.load_tables()

        ######################################
        # Functionalities for get new skills #
        ######################################

        self.list_of_resources = ["https://elearningindustry.com/prepare-yourself-for-a-job-interview-6-top-online-resources",
                                  "https://www.prospects.ac.uk/careers-advice/interview-tips/how-to-prepare-for-an-interview",
                                  "https://www.careerbuilder.com/advice/topic/interviews",
                                  "https://www.prospects.ac.uk/careers-advice/applying-for-jobs/write-a-successful-job-application",
                                  "https://www.thebalancecareers.com/how-to-apply-for-jobs-online-2061598",
                                  "https://help.open.ac.uk/applying-for-jobs-an-overview-of-the-process"]

        self.list_resources.clicked.connect(self.view_resource_clicked)
        self.list_resources.clear()
        for item in self.list_of_resources:
            self.list_resources.addItem(item)

        ######################
        # User settings page #
        ######################

        self.lbl_details_updated.setHidden(True)
        self.btn_save.clicked.connect(self.save_account)
        self.pushButton.clicked.connect(self.show_delete_popup)
        self.btn_skill_2.clicked.connect(self.delete_account)
        self.btn_skill_3.clicked.connect(self.show_delete_popup)

    ###########################
    # Functions for main menu #
    ###########################

    def open_find_jobs(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.FIND_JOB_RESOURCES)
        self.choose_item_widget.setHidden(True)

    def open_jobs_found(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.JOBS_FOUND_MAIN)
        self.choose_item_widget.setHidden(True)

    def open_settings(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.SETTINGS_MAIN)
        self.choose_item_widget_2.hide()
        self.choose_item_widget.setHidden(True)
        user_data = lg.get_user(self.username)
        for user in user_data:
            self.edit_full_name.setText(user[2])
            self.edit_email.setText(user[1])
            self.edit_password.setText(user[3])

    def open_home(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.HOME_PAGE_MAIN)
        self.choose_item_widget.setHidden(True)

    # Functions for the four main buttons
    def open_portfolio(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.USER_PORTFOLIO_MAIN)
        self.choose_item_widget.setHidden(True)

    def open_skills(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.ACQUIRE_NEW_SKILLS_MAIN)

    def open_jobs(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.FIND_A_JOB_MAIN)

    def open_plan(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.YOUR_ACTION_PLAN)

    def quit_app(self):
        self.close()

    # Toggle menu function
    def toggle_menu(self):

        if not self.menu_toggled:
            self.menu_toggled = True
            self.menu_widget.setHidden(False)
            print('menu toggled')
        else:
            self.menu_toggled = False
            self.menu_widget.setHidden(True)
            print('menu untoggled')

    ###############################
    # Functions for User Portfolio#
    ###############################

    # Update lists to include new skills
    def update_lists(self):
        self.skills_list.clear()
        self.education_list.clear()
        self.experience_list.clear()

        for ski in sk.check_skills():
            self.skills_list.addItem(''.join(ski[0]))
        for educ in ed.check_edu():
            self.education_list.addItem(''.join(educ[0]))
        for expi in exp.check_work_exp():
            self.experience_list.addItem(''.join(expi[0]))

    def find_resources_clicked(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.ACQUIRE_NEW_SKILLS_MAIN)

    # Skill clicked
    def skill_clicked(self, item):
        self.skill = item.text()
        skills = sk.get_skill(self.skill)
        self.lbl_item_category.setText(self.skill)
        desc = 'Description: \n'
        for skill in skills:
            for attr in skill:
                desc += str(attr)
                desc += '\n'
        self.lbl_item_desc.setText(desc)
        self.ALL_STACKED_PAGES.setCurrentWidget(self.PORTFOLIO_VIEW_ITEM_MAIN)

    def edu_clicked(self, item):
        self.eduu = item.text()
        educations = ed.get_education(self.eduu)
        self.lbl_item_category.setText(self.eduu)
        desc = 'Description: \n'
        for education in educations:
            for attr in education:
                desc += str(attr)
                desc += '\n'
        self.lbl_item_desc.setText(desc)
        self.ALL_STACKED_PAGES.setCurrentWidget(self.PORTFOLIO_VIEW_ITEM_MAIN)

    def work_clicked(self, item):
        self.job = item.text()
        jobs = exp.get_exp(self.job)
        self.lbl_item_category.setText(self.job)
        desc = 'Description: \n'
        for work in jobs:
            for attr in work:
                desc += str(attr)
                desc += '\n'
        self.lbl_item_desc.setText(desc)
        self.ALL_STACKED_PAGES.setCurrentWidget(self.PORTFOLIO_VIEW_ITEM_MAIN)

    # Add skill functions
    def add_item(self):
        self.choose_item_widget.setHidden(False)

    def add_skill(self):
        self.choose_item_widget.setHidden(True)
        self.ALL_STACKED_PAGES.setCurrentWidget(self.ADD_SKILL_MAIN)

    def add_education(self):
        self.choose_item_widget.setHidden(True)
        self.ALL_STACKED_PAGES.setCurrentWidget(self.ADD_EDUCATION_MAIN)

    def add_experience(self):
        self.choose_item_widget.setHidden(True)
        self.ALL_STACKED_PAGES.setCurrentWidget(self.ADD_EXPERIENCE_MAIN)

    def add_to_skill_list(self):
        skill = []
        skillname = self.edit_skill.text()
        skilldesc = self.edit_skill_description.toPlainText()
        inference = '0'
        skill.append(skillname)
        skill.append(skilldesc)
        skill.append(inference)
        self.skills_to_add.append(skill)
        self.new_skills_list.addItem(skill[0])

        self.edit_skill.clear()
        self.edit_skill_description.clear()

    def send_skills(self):
        sk.enter_new_skill(self.skills_to_add)
        self.new_skills_list.clear()
        self.ALL_STACKED_PAGES.setCurrentWidget(self.USER_PORTFOLIO_MAIN)
        self.update_lists()

    # Add Education Functions

    def add_to_edu_list(self):
        edu = []
        eduname = self.edit_name.text()
        edulvl = self.edit_level.text()
        eduloc = self.edit_location.text()
        date = self.choose_date.date().toString('dd/MM/yyyy')
        edu.append(eduname)
        edu.append(edulvl)
        edu.append(eduloc)
        edu.append(date)
        self.edu_to_add.append(edu)
        self.new_education_list.addItem(edu[0])

        self.edit_name.clear()
        self.edit_level.clear()
        self.edit_location.clear()

    def send_education(self):
        ed.enter_new_edu(self.edu_to_add)
        self.new_education_list.clear()
        self.ALL_STACKED_PAGES.setCurrentWidget(self.USER_PORTFOLIO_MAIN)
        self.update_lists()

    # Add work experience functions

    def add_to_work_list(self):
        wrok = []
        job_title = self.edit_job_title.text()
        job_desc = self.edit_job_description.toPlainText()
        salary = self.edit_salary.text()
        startdate = self.choose_start_date.date().toString('dd/MM/yyyy')
        enddate = self.choose_end_date.date().toString('dd/MM/yyyy')
        location = self.edit_location_3.text()
        wrok.append(job_title)
        wrok.append(job_desc)
        wrok.append(salary)
        wrok.append(startdate)
        wrok.append(enddate)
        wrok.append(location)
        self.work_to_add.append(wrok)
        self.new_jobs_list.addItem(wrok[0])

        self.edit_job_title.clear()
        self.edit_job_description.clear()
        self.edit_salary.clear()

    def send_work_exp(self):
        exp.enter_new_work(self.work_to_add)
        self.new_jobs_list.clear()
        self.ALL_STACKED_PAGES.setCurrentWidget(self.USER_PORTFOLIO_MAIN)
        self.update_lists()

    def skill_edit_clicked(self):
        skillset = sk.get_skill(self.edit_skill_dropdown.currentText())
        for skill in skillset:
            self.edit_skill.setText(''.join(skill[0]))
            self.edit_skill_description.setText(''.join(skill[1]))

    def edu_edit_clicked(self):
        eduset = ed.get_education(self.edit_education_dropdown.currentText())
        for educ in eduset:
            self.edit_name.setText(''.join(educ[0]))
            self.edit_level.setText(''.join(educ[1]))
            self.edit_location.setText(''.join(educ[2]))

    def job_edit_clicked(self):
        jobset = exp.get_exp(self.edit_job_dropdown.currentText())
        for jobb in jobset:
            self.edit_job_title.setText(jobb[0])
            self.edit_job_description.setText(jobb[1])
            self.edit_salary.setText(jobb[2])
            self.edit_location_3.setText(jobb[5])

    # Delete skills edu and experience
    def delete_skill_clicked(self):
        sk.delete_skill(self.edit_skill.text())
        self.ALL_STACKED_PAGES.setCurrentWidget(self.USER_PORTFOLIO_MAIN)
        self.update_lists()

    def delete_education_clicked(self):
        ed.delete_edu(self.edit_name)
        self.ALL_STACKED_PAGES.setCurrentWidget(self.USER_PORTFOLIO_MAIN)
        self.update_lists()

    def delete_experience_clicked(self):
        exp.delete_work(self.edit_job_title.text())
        self.ALL_STACKED_PAGES.setCurrentWidget(self.USER_PORTFOLIO_MAIN)
        self.update_lists()

    ##########################
    # Functions for find job #
    ##########################

    def job_clicked(self, item):
        is_empty, job_got = jb.get_job(item.text())
        for jobs in job_got:
            title, descr, comp, post, deadl, salary, location, skills, url = jobs

        if is_empty != 0:
            self.ALL_STACKED_PAGES.setCurrentWidget(self.VIEW_JOB_DETAIL_MAIN)
            self.lbl_item_category_2.setText(title)
            self.lbl_item_desc_3.setText(descr)
            self.lbl_item_desc_4.setText(url)
            self.details_table.setItem(0, 0, QTableWidgetItem(salary))
            self.details_table.setItem(1, 0, QTableWidgetItem(location))
            self.details_table.setItem(2, 0, QTableWidgetItem(post))
            self.details_table.setItem(3, 0, QTableWidgetItem(deadl))
            self.details_table.setItem(4, 0, QTableWidgetItem(comp))
            self.list_skills.clear()
            self.list_skills.addItem(skills)

    def jobs_found_clicked(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.JOBS_FOUND_MAIN)

    def find_a_job_clicked(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.FIND_JOB_RESOURCES)

    def add_new_job_clicked(self):
        self.ALL_STACKED_PAGES.setCurrentWidget(self.ADD_EDIT_JOB_MAIN)

    def edit_job_clicked(self):
        jobset = jb.get_job(self.edit_job_dropdown_2.currentText())
        for jooob in jobset[1]:
            self.edit_job_title_2.setText(jooob[0])
            self.edit_job_description_2.setText(jooob[1])
            self.edit_company.setText(jooob[2])
            self.edit_salary_2.setText(jooob[5])
            self.edit_location_4.setText(jooob[6])
            self.edit_skill_2.setText(jooob[7])
            self.edit_advert_link.setText(jooob[8])

    def save_job(self):
        job = [self.edit_job_title_2.text(), self.edit_job_description_2.toPlainText(), self.edit_company.text(),
               self.date_posted.text(), self.deadline_date.text(), self.edit_salary_2.text(),
               self.edit_location_4.text(), self.edit_skill_2.text(), self.edit_advert_link.text()]

        jb.enter_new_job(job)
        self.edit_job_title_2.clear()
        self.edit_job_description_2.clear()
        self.edit_company.clear()
        self.edit_salary_2.clear()
        self.edit_location_4.clear()
        self.edit_skill_2.clear()
        self.edit_advert_link.clear()

        self.ALL_STACKED_PAGES.setCurrentWidget(self.JOBS_FOUND_MAIN)

    def delete_job_clicked(self):
        jb.delete_job(self.edit_job_title_2.text())
        self.ALL_STACKED_PAGES.setCurrentWidget(self.JOBS_FOUND_MAIN)

    # Find job
    def visit_job_resource(self):
        selected_urls = self.list_resources_3.selectedItems()
        for item in selected_urls:
            url = item.text()
        webbrowser.open_new_tab(url)



    #############################
    # Functions for Action Plan #
    #############################

    def save_tables(self):
        action_plan_table = []

        rows = self.action_plan_table.rowCount()
        cols = self.action_plan_table.columnCount()

        for row in range(rows):
            column_value = []
            for column in range(cols):
                item = self.action_plan_table.item(row, column)
                if item is None:
                    column_value.append(".")
                else:
                    column_value.append(item.text())
            action_plan_table.append(column_value)
        print(action_plan_table)
        ap.save_table(action_plan_table)


    def load_tables(self):
        table_actions = ap.load_table()
        row = 0
        for data_rows in table_actions:
            col = 0
            for cell in data_rows:
                if cell != '.':
                    self.action_plan_table.setItem(row, col, QTableWidgetItem(cell))
                col += 1
            row += 1


        table_jobs = jb.check_jobs()
        row = 0
        for data_rows in table_jobs:
            col = 0
            for cell in data_rows:
                self.jobs_found_table.setItem(row, col, QTableWidgetItem(str(cell)))
                col += 1
            row += 1
    ################################
    # Functions for get new skills #
    ################################

    def view_resource_clicked(self):
        selected_urls = self.list_resources.selectedItems()
        for item in selected_urls:
            url = item.text()
        webbrowser.open_new_tab(url)

    ###################################
    # Function for user settings page #
    ###################################

    def save_account(self):
        name = self.edit_full_name.text()
        email = self.edit_email.text()
        password = self.edit_password.text()

        lg.enter_new_user(name, email, password)
        lg.delete_user(name, password)
        self.lbl_details_updated.setHidden(False)

    def delete_account(self):
        lg.delete_user(self.edit_full_name.text(), self.edit_password.text())
        self.close()

    def show_delete_popup(self):
        if self.popup_hidden:
            self.choose_item_widget_2.setHidden(False)
            self.popup_hidden = False
        else:
            self.choose_item_widget_2.setHidden(True)
            self.popup_hidden = True


app = QApplication(sys.argv)
lg.create_table()
window = Welcome_Screen()
window.show()
sys.exit(app.exec_())