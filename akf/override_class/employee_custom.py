import frappe
from erpnext.setup.doctype.employee.employee import Employee

class EmployeeCustom(Employee):
    def validate(self):
        frappe.msgprint(frappe.as_json(self))