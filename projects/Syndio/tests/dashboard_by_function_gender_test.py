
description = 'Verify when Grouped by Function and Gender tab is selected, text displayed on page is correct and correct tab is highlighted. '

pages = ['dashboard_page']


def test_by_gender(data):
    dashboard_page.navigate()
    wait_for_element_present(dashboard_page.tab_gender)
    dashboard_page.check_active_tab("Gender")
    assert_element_text(dashboard_page.pay_equity_gap_label, "Pay Equity Gap")
    assert_element_text(dashboard_page.pay_equity_gap_p, "Women earn 96¢ for every $1 earned by comparable Men")
    assert_element_text(dashboard_page.employees_comparison_label, "Employees in Comparison")
    assert_element_text(dashboard_page.employees_comparison_p, "Women make up 41% of employees")
    assert_element_text(dashboard_page.budget_label, "Budget")
    assert_element_text(dashboard_page.budget_p, "$235,000 minimum recommended budget to reduce pay equity gap")


