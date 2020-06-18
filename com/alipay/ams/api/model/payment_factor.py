#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PaymentFactor(object):
    def __init__(self):
        self.__is_payment_evaluation = None
        self.__in_store_payment_scenario = None

    @property
    def is_payment_evaluation(self):
        return self.__is_payment_evaluation

    @is_payment_evaluation.setter
    def is_payment_evaluation(self, value):
        self.__is_payment_evaluation = value

    @property
    def in_store_payment_scenario(self):
        return self.__in_store_payment_scenario

    @in_store_payment_scenario.setter
    def in_store_payment_scenario(self, value):
        self.__in_store_payment_scenario = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "is_payment_evaluation") and self.__is_payment_evaluation:
            params['isPaymentEvaluation'] = self.is_payment_evaluation

        if hasattr(self, "in_store_payment_scenario") and self.in_store_payment_scenario:
            params['inStorePaymentScenario'] = self.in_store_payment_scenario

        return params
