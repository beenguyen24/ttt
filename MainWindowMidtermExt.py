from MainWindowMidterm import Ui_MainWindow


class MainWindowMidtermExt(Ui_MainWindow):
    salary_intern = 2000000
    salary_fresher = 10000000
    salary_junior = 15000000
    salary_senior = 30000000

    num_intern = 0
    num_fresher = 0
    num_junior = 0
    num_senior = 0

    salaryofsenior = 0
    salaryoffresher = 0
    salaryofjunior = 0
    salaryofintern = 0

    count_of_all_employees = 0
    total = 0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonSalary.clicked.connect(self.process_salary)
        self.pushButtonExit.clicked.connect(self.MainWindow.close)
    def process_salary(self):
        n_employee = 0
        # Kiểm tra dữ liệu nhập có phải là số nguyên dương không
        try:
            n_employee = int(self.lineEditNumberOfEmployee.text())
            if n_employee <=0:
                print("The number of employees must be a positive number.")
        except:
            self.lineEditCountToFall.setText("Invalid Value")
            print("Error!!!")
            return
        # Kiểm tra xem người dùng đã chọn cấp bậc nhân viên chưa
        if not (self.radioButtonIntern.isChecked() or
                self.radioButtonJunior.isChecked() or
                self.radioButtonFresher.isChecked() or
                self.radioButtonSenior.isChecked()):
            self.lineEditCountofall.setText("No level selected")
            print("Error: No employee level selected.")
            return
        # Tính lương cho từng cấp bậc
        if self.radioButtonIntern.isChecked():
            salary_intern = n_employee * self.salary_Intern
            self.num_intern = self.num_intern + n_employee
            self.salaryofintern = self.salaryofintern + salary_intern
        elif self.radioButtonJunior.isChecked():
            salary_junior = n_employee * self.salary_junior
            self.num_junior = self.num_junior + n_employee
            self.salaryofjunior = self.salaryofjunior + salary_junior
        elif self.radioButtonFresher.isChecked():
            salary_fresher = n_employee * self.salary_fresher
            self.num_fresher = self.num_fresher + n_employee
            self.salaryoffresher = self.salaryoffresher + salary_fresher
        elif self.radioButtonSenior.isChecked():
            salary_senior = n_employee * self.salary_senior
            self.num_senior = self.num_senior + n_employee
            self.salaryofsenior = self.salaryofsenior + salary_senior
        # Tính tổng số nhân viên và tổng lương
        self.count_of_all_employees = self.num_senior + self.num_fresher + self.num_junior + self.num_intern
        self.total = self.salaryofintern + self.salaryofjunior + self.salaryoffresher + self.salaryofsenior
        # Cập nhật giao diện với kết quả tính toán
        self.lineEditNumberOfIntern.setText(str(self.num_intern))
        self.lineEditNumberOfJunior.setText(str(self.num_junior))
        self.lineEditNumberOfSenior.setText(str(self.num_senior))
        self.lineEditNumberOfFresher.setText(str(self.num_fresher))
        self.lineEditCostOfAll.setText(str(self.count_of_all_employees))
        self.lineEditSalaryFresher.setText(str(self.salaryoffresher))
        self.lineEditSalaryJunior.setText(str(self.salaryofjunior))
        self.lineEditSalaryIntern.setText(str(self.salaryofintern))
        self.lineEditSalarySenior.setText(str(self.salaryofsenior))
        self.lineEditCountToFall.setText(str(self.total))
