import os
from nemlite import standards as st


def declare_names():
    aemo_naming = st.Naming(base_filename='/{}_{}{}010000.CSV',
                            col_datetime_applicable='INTERVAL_DATETIME',
                            col_date_applicable='SETTLEMENTDATE',
                            col_date_changed='LASTCHANGED',
                            cols_bid_cap_name_list=['BANDAVAIL1', 'BANDAVAIL2', 'BANDAVAIL3', 'BANDAVAIL4',
                                                    'BANDAVAIL5', 'BANDAVAIL6', 'BANDAVAIL7', 'BANDAVAIL8',
                                                    'BANDAVAIL9', 'BANDAVAIL10'],
                            cols_bid_price_name_list=['PRICEBAND1', 'PRICEBAND2', 'PRICEBAND3', 'PRICEBAND4',
                                                      'PRICEBAND5', 'PRICEBAND6', 'PRICEBAND7', 'PRICEBAND8',
                                                      'PRICEBAND9', 'PRICEBAND10'],
                            col_unit_name='DUID',
                            col_unit_max_output='MAXAVAIL',
                            col_enablement_min='ENABLEMENTMIN',
                            col_enablement_max='ENABLEMENTMAX',
                            col_bid_type='BIDTYPE',
                            col_capacity_band_number='CAPACITYBAND',
                            col_price_band_number='PRICEBAND',
                            col_bid_value='BID',
                            col_enablement_type='ENABLEMENTTYPE',
                            col_enablement_value='ENABLEMENTVALUE',
                            col_low_break_point='LOWBREAKPOINT',
                            col_high_break_point='HIGHBREAKPOINT',
                            col_lhs_coefficients='LHSCOEFFICIENTS',
                            col_rhs_constant='RHSCONSTANT',
                            col_upper_bound='UPPERBOUND',
                            col_lower_bound='LOWERBOUND',
                            col_variable_index='INDEX',
                            col_energy_variable_index='ENERGYINDEX',
                            col_max_unit_energy='MAXENERGY',
                            col_constraint_row_index='ROWINDEX',
                            col_fcas_integer_variable='FCASINTEGER',
                            type_energy='ENERGY',
                            type_fcas='FCAS',
                            col_inter_id='INTERCONNECTORID',
                            col_import_limit='IMPORTLIMIT',
                            col_export_limit='EXPORTLIMIT',
                            col_fcas_import_limit='FCASIMPORTLIMIT',
                            col_fcas_export_limit='FCASEXPORTLIMIT',
                            list_fcas_types=['LOWER5MIN', 'LOWER60SEC', 'LOWER6SEC', 'RAISE5MIN', 'RAISE60SEC',
                                             'RAISE6SEC', 'LOWERREG', 'RAISEREG'],
                            col_gen_req='TOTALDEMAND',
                            col_lower_5min_req='LOWER5MINLOCALDISPATCH',
                            col_lower_60sec_req='LOWER60SECLOCALDISPATCH',
                            col_lower_6sec_req='LOWER6SECLOCALDISPATCH',
                            col_raise_5min_req='RAISE5MINLOCALDISPATCH',
                            col_raise_60sec_req='RAISE60SECLOCALDISPATCH',
                            col_raise_6sec_req='RAISE6SECLOCALDISPATCH',
                            col_lower_reg_req='LOWERREGLOCALDISPATCH',
                            col_raise_req_req='RAISEREGLOCALDISPATCH',
                            col_region_id='REGIONID',
                            col_region_constraint_type='CONSTRAINTTYPE',
                            col_region_constraint_value='RHSCONSTANT',
                            col_end_date='END_DATE',
                            col_contribution_coefficients='CONTRACOE',
                            col_region_from='REGIONFROM',
                            col_region_to='REGIONTO',
                            col_direction='DIRECTION',
                            col_limit_value='LIMIT',
                            col_enquality_type='ENQUALITYTYPE',
                            col_price='PRICE',
                            col_loss_factor='TRANSMISSIONLOSSFACTOR',
                            col_dispatch_type='DISPATCHTYPE',
                            type_load='LOAD',
                            type_gen='GENERATOR',
                            col_pool_id='POOLID')
    return aemo_naming