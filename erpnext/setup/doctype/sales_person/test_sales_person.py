# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

EXTRA_TEST_RECORD_DEPENDENCIES = ["Employee"]

import frappe

test_records = frappe.get_test_records("Sales Person")

IGNORE_TEST_RECORD_DEPENDENCIES = ["Item Group"]
