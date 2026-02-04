import frappe
from frappe import _

import frappe

@frappe.whitelist()
def total_net_profit():
    """
    Returns total net profit: sum of submitted Sales Invoices minus sum of submitted Purchase Invoices.
    """
    # Total sales
    total_sales = frappe.db.sql("""
        SELECT SUM(base_grand_total) 
        FROM `tabSales Invoice` 
        WHERE docstatus = 1
    """)[0][0] or 0

    # Total purchases / expenses
    total_expenses = frappe.db.sql("""
        SELECT SUM(base_grand_total) 
        FROM `tabPurchase Invoice` 
        WHERE docstatus = 1
    """)[0][0] or 0

    net_profit = total_sales - total_expenses

    return {
        "value": net_profit,
        "fieldtype": "Currency",
        "route": ["Report", "Profit and Loss"],
        "route_options": {}
    }
