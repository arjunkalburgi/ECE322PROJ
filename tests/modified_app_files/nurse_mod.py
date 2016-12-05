import sys

def newChartFlow(nur, patient):
	print "New chart has been selected"
	return nur.newChart(patient["hcno"])

def selectChart(nur, patient, boolalreadyopen, chartToOpen, faultyID):
    if nur.checkIfPatientHasOpenChart(patient["hcno"]) is not None:
        if boolalreadyopen:
    # return open chart
            return nur.checkIfPatientHasOpenChart(patient["hcno"])

    while(True):
        chartId = chartToOpen
        if chartId == "new":
    # return new chart id
            return newChartFlow(nur, patient)
        else:
    # return chart id
            if not faultyID:
                print("There was a problem, please type the chartid. ")
            else:
                return chartId