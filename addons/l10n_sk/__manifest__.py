# -*- coding: utf-8 -*-

{
    'name': 'Slovak - Accounting',
    'version': '14.0.1.0.0',
    'author': '26HOUSE',
    'website': 'http://www.26house.com',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
Slovakia accounting chart and localization.

Tento modul definuje:
• Slovenskú účtovú osnovu za rok 2020

• Základné sadzby pre DPH z predaja a nákupu

• Základné fiškálne pozície pre slovenskú legislatívu

 
Pre viac informácií kontaktujte info@26house.com alebo navštívte https://www.26house.com.
    
    """,
    'depends': [
        'account',
        'base_iban',
        'base_vat',
        'l10n_multilang',
    ],
    'data': [
              'data/l10n_sk_coa_data.xml',
              'data/account.account.template.csv',
              'data/account.group.template.csv',
              'data/l10n_sk_coa_post_data.xml',
              'data/account_data.xml',
              'data/account_tax_data.xml',
              'data/account_fiscal_position_data.xml',
              'data/account_chart_template_data.xml'
    ],
    'post_init_hook': '_preserve_tag_on_taxes',
}
