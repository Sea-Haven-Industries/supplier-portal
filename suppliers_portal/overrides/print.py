import frappe
from frappe.utils import flt, money_in_words


@frappe.whitelist()
def amount_in_words_with_asterisks(amount):
	amount = flt(amount)
	amount_in_words = money_in_words(amount)[4:-6]
	if amount % 1 == 0:
		return f"{amount_in_words + ' and Zero Cents ':*<70}"
	return f"{amount_in_words + 's ':*<84}"
