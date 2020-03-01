from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class StartPage(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self): # initialises first round holding and order cost, these are written over before first round ends
        self.player.hcA = 0
        self.player.ocA = 0
        self.player.bcA = 0
        self.player.hcB = 0
        self.player.ocB = 0
        self.player.bcB = 0
        self.player.hcC = 0
        self.player.ocC = 0
        self.player.bcC = 0


class MyPage(Page):

#    timeout_seconds = 10

    form_model = 'player'
    if Constants.simple == 'yes':
        form_fields = ['QB']
    else:
        form_fields = ['QA','QB','QC']

    def vars_for_template(self):

        if self.round_number == 1:
            prevQ = [0,0,0]
        else:
            prevQ = [self.player.in_round(self.round_number - 1).QA,
                     self.player.in_round(self.round_number - 1).QB,
                     self.player.in_round(self.round_number - 1).QC]

        DA = self.session.vars['demandA'][self.round_number - 1] / 365  # demand for this round
        DB = self.session.vars['demandB'][self.round_number - 1] / 365  # demand for this round
        DC = self.session.vars['demandC'][self.round_number - 1] / 365  # demand for this round

        allIA = [Constants.initialinventory]
        allIB = [Constants.initialinventory]
        allIC = [Constants.initialinventory]
        i = 1
        [thcA, tocA, tbcA] = [(Constants.holdingcost[0] / 365) * (Constants.initialinventory), 0, 0]  # tot. costs
        [thcB, tocB, tbcB] = [(Constants.holdingcost[1] / 365) * (Constants.initialinventory), 0, 0]  # tot. costs
        [thcC, tocC, tbcC] = [(Constants.holdingcost[2] / 365) * (Constants.initialinventory), 0, 0]  # tot. costs
        while i < self.round_number:
            allIA.append(self.player.in_round(i).IA)
            allIB.append(self.player.in_round(i).IB)
            allIC.append(self.player.in_round(i).IC)
            thcA += self.player.in_round(i).hcA
            tocA += self.player.in_round(i).ocA
            tbcA += self.player.in_round(i).bcA
            thcB += self.player.in_round(i).hcB
            tocB += self.player.in_round(i).ocB
            tbcB += self.player.in_round(i).bcB
            thcC += self.player.in_round(i).hcC
            tocC += self.player.in_round(i).ocC
            tbcC += self.player.in_round(i).bcC
            i += 1

        # DETERMINE AVERAGE SERVICE LEVEL

        return { # these are list variables that are accessed by index 0,1,2
            'prevQ': prevQ,
            'allIA': allIA,
            'allIB': allIB,
            'allIC': allIC,
            'I': [allIA[self.round_number-1],
                  allIB[self.round_number-1],
                  allIC[self.round_number-1]],
            'D': [DA, DB, DC],
            'thc': [thcA, thcB, thcC],
            'toc': [tocA, tocB, tocC],
            'tbc': [tbcA, tbcB, tbcC],
            'holdingcostpx': [str(thcA / (thcA + tocA + tbcA) * 100)+"%",
                              str(thcB / (thcB + tocB + tbcB) * 100) + "%",
                              str(thcC / (thcC + tocC + tbcC) * 100) + "%"],
            'orderingcostpx': [str(tocA / (thcA + tocA + tbcA) * 100) + "%",
                               str(tocB / (thcB + tocB + tbcB) * 100) + "%",
                               str(tocC / (thcC + tocC + tbcC) * 100) + "%"],
            'backlogcostpx': [str(tbcA / (thcA + tocA + tbcA) * 100) + "%",
                              str(tbcB / (thcB + tocB + tbcB) * 100) + "%",
                              str(tbcC / (thcC + tocC + tbcC) * 100) + "%"]
        }

    def before_next_page(self):

        if self.player.QA > 0:
            self.player.ocA = Constants.ordercost
        else:
            self.player.ocA = 0

        if self.player.QB > 0:
            self.player.ocB = Constants.ordercost
        else:
            self.player.ocB = 0

        if self.player.QC > 0:
            self.player.ocC = Constants.ordercost
        else:
            self.player.ocC = 0

        DA = self.session.vars['demandA'][self.round_number - 1] / 365
        DB = self.session.vars['demandB'][self.round_number - 1] / 365
        DC = self.session.vars['demandC'][self.round_number - 1] / 365

        if self.round_number == 1:
            self.player.IA = Constants.initialinventory + self.player.QA - DA
            self.player.IB = Constants.initialinventory + self.player.QB - DB
            self.player.IC = Constants.initialinventory + self.player.QC - DC
        else:
            self.player.IA = self.player.in_round(self.round_number - 1).IA + self.player.QA - DA
            self.player.IB = self.player.in_round(self.round_number - 1).IB + self.player.QB - DB
            self.player.IC = self.player.in_round(self.round_number - 1).IC + self.player.QC - DC

        self.player.hcA = max([(self.player.IA)*(Constants.holdingcost[0] / 365), 0])
        self.player.bcA = max([(-1)*(self.player.IA)*(Constants.backlogcost[0] / 365), 0])
        self.player.hcB = max([(self.player.IB)*(Constants.holdingcost[1] / 365), 0])
        self.player.bcB = max([(-1)*(self.player.IB)*(Constants.backlogcost[1] / 365), 0])
        self.player.hcC = max([(self.player.IC) * (Constants.holdingcost[2] / 365), 0])
        self.player.bcC = max([(-1) * (self.player.IC) * (Constants.backlogcost[2] / 365), 0])
#       self.player.servicelevel =


class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [StartPage, MyPage, Results]