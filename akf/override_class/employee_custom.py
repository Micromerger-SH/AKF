import frappe
from erpnext.setup.doctype.employee.employee import Employee

class EmployeeCustom(Employee):
    def validate(self):
        from erpnext.controllers.status_updater import validate_status
        validate_status(self.status, ["Active", "Inactive", "Suspended", "Left"])