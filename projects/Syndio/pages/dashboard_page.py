from golem import actions


active_tab = ('css', 'button.tab.tab-active', 'active_tab')

budget_label = ('css', '#budget > label', 'budget_label')

budget_p = ('css', '#budget > p', 'budget_p')

disabled_dropdown_option = ('css', 'li.disabled', 'disabled_dropdown_option')

dropdown_button = ('id', 'dropdown-button', 'dropdown_button')

employees_comparison_label = ('css', '#employeeComparison > label', 'employees_comparison_label')

employees_comparison_p = ('css', '#employeeComparison > p', 'employees_comparison_p')

group_by_function = ('id', 'a9f6a4b7-d03c-4a45-b64b-791e054f36b8', 'group_by_function')

group_by_role = ('id', 'f1b01b57-3147-476a-a632-0c10ad2a3c1a', 'group_by_role')

pay_equity_gap_label = ('css', '#payEquityGap > label', 'pay_equity_gap_label')

pay_equity_gap_p = ('css', '#payEquityGap > p', 'pay_equity_gap_p')

tab_gender = ('id', 'tab-gender', 'tab_gender')

tab_race = ('id', 'tab-race', 'tab_race')

def check_active_tab(tab_name):
    actions.assert_element_text(active_tab, tab_name)


def check_disabled_dropdown_option(option_name):
    actions.assert_element_text(disabled_dropdown_option, option_name)


def navigate():
    actions.navigate("http://localhost:3000/")
