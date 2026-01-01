# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re


class ResUsers(models.Model):
    _inherit = 'res.users'

    ssn = fields.Char(
        string='Social Security Number',
        size=12,
        help='Enter 12-digit Social Security Number',
        tracking=True,
    )

    @api.constrains('ssn')
    def _check_ssn_format(self):
        """Constraint to ensure SSN is exactly 12 digits"""
        for user in self:
            if user.ssn:
                # Remove any whitespace or dashes that users might enter
                cleaned_ssn = re.sub(r'\s+|-', '', user.ssn)

                # Check if it's exactly 12 digits and contains only numbers
                if not (cleaned_ssn.isdigit() and len(cleaned_ssn) == 12):
                    raise ValidationError(_(
                        'Social Security Number must contain exactly 12 digits. '
                        'Format: 123456789012'
                    ))
                # Update the field with cleaned value (without separators)
                if user.ssn != cleaned_ssn:
                    user.ssn = cleaned_ssn

    # Alternative: Using SQL constraint for database-level validation
    # Uncomment if you prefer database-level constraint
    # _sql_constraints = [
    #     ('ssn_format_check',
    #      'CHECK (ssn IS NULL OR (ssn ~ \'^[0-9]{12}$\' AND length(ssn) = 12))',
    #      'Social Security Number must contain exactly 12 digits.')
    # ]