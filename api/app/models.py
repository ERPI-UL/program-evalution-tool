import os
import uuid
from datetime import date
from owlready2 import *
onto = get_ontology("./app/static/ProgramImpactEvaluationOntology-wInstance2.owl").load()

def getProgrammes():
    data = []
    programs = onto.Program.instances()
    for program in programs:
        tmp_formulation = {}
        tmp_formulation['iri'] = program.iri
        tmp_formulation['name'] = program.name
        if isinstance(program.hasStartDate, int):
            tmp_formulation['startDate'] = date.fromtimestamp(program.hasStartDate).isoformat()
        else:
            tmp_formulation['startDate'] = program.hasStartDate
        if isinstance(program.hasEndDate, int):
            tmp_formulation['endDate'] = date.fromtimestamp(program.hasEndDate).isoformat()
        else:
            tmp_formulation['endDate'] = program.hasEndDate
        data.append(tmp_formulation)
    return data

def getProgram(name):
    iri = f"http://purl.org/pieo#{name}"
    Program = IRIS[iri]
    data = {}
    data['iri'] = Program.iri
    data['name'] = Program.name
    if isinstance(Program.hasStartDate, int):
        data['startDate'] = date.fromtimestamp(Program.hasStartDate).isoformat()
    else:
        data['startDate'] = Program.hasStartDate
    if isinstance(Program.hasEndDate, int):
        data['endDate'] = date.fromtimestamp(Program.hasEndDate).isoformat()
    else:
        data['endDate'] = Program.hasEndDate
    #data['description'] = Program.
    return data

def getIndicators():
    data = []
    indicators = onto.Indicator.instances()
    print(indicators)
    for indicator in indicators:
        tmp_formulation = {}
        tmp_formulation['iri'] = indicator.iri
        tmp_formulation['name'] = indicator.name
        tmp_formulation['decription'] = indicator.comment.en.first()
        tmp_formulation['resultChainStep'] = indicator.hasResultChainStep
        tmp_formulation['indType'] = indicator.collect
        tmp_formulation['origin'] = indicator.hasOrigin
        data.append(tmp_formulation)
    return data

def getIndicator(name):
    iri = f"http://purl.org/pieo#{name}"
    indicator = IRIS[iri]
    data = {}
    data['iri'] = indicator.iri
    data['name'] = indicator.name
    data['decription'] = indicator.comment.en.first()
    data['resultChainStep'] = indicator.hasResultChainStep
    return data

def formulations():
    data = []
    formulations = onto.Formulation.instances()
    for formul in formulations:
        tmp_formulation = {}
        tmp_formulation['iri'] = formul.iri
        tmp_formulation['name'] = formul.name
        tmp_formulation['surfactantQte'] = formul.hasTotalSurfactantQuantity
        tmp_formulation['thickenerQte'] = formul.hasTotalThickenerQuantity
        tmp_formulation['surfactantNb'] = formul.hasNbSurfactantIng
        tmp_formulation['oilyPhaseQte'] = formul.hasTotalOilyPhase
        data.append(tmp_formulation)
    return data

def formulation(iri):
    
    Formulation = IRIS[iri]
    dosages = Formulation.hasDosage
    dos = []
    data = {}
    data['iri'] = Formulation.iri
    data['name'] = Formulation.name
    data['surfactQte'] = Formulation.hasTotalSurfactantQuantity
    data['thickenerQte']= Formulation.hasTotalThickenerQuantity
    data['surfactNb']= Formulation.hasNbSurfactantIng
    data['oilyPhaseQte']= Formulation.hasTotalOilyPhase
    data['stability'] = Formulation.hasProductStability
    data['oiliness'] = Formulation.hasProductOiliness
    data['viscosity'] = Formulation.hasProductViscosity
    for Dosage in dosages:
        tmp_dosage = {}
        tmp_dosage['ing'] = Dosage.hasIngredient
        tmp_dosage['qte'] = Dosage.hasQuantity
        dos.append(tmp_dosage)
    data['dosages'] = dos
    return data

def heuristicsValidatedByFormulation(iri):
    Formulation = IRIS[iri]
    heuristics = Formulation.isValidatedBy
    heurs = []
    for Heuristic in heuristics:
        tmp_heur = {}
        tmp_heur['id'] = Heuristic.name
        tmp_heur['description'] = Heuristic.hasHeuristicDescription
        tmp_heur['prodProperty'] = Heuristic.hasHeuristicProdProp
        heurs.append(tmp_heur)
    return heurs

def heuristics():
    data = []
    heuristics = onto.Heuristic.instances()
    for Heuristic in heuristics:
        tmp_heuristic = {}
        tmp_heuristic['iri'] = Heuristic.iri
        tmp_heuristic['name'] = Heuristic.name
        tmp_heuristic['description'] = Heuristic.hasHeuristicDescription
        tmp_heuristic['ingType'] = Heuristic.hasHeuristicIngType
        tmp_heuristic['ingProperty'] = Heuristic.hasHeuristicIngProp
        tmp_heuristic['prodProperty'] = Heuristic.hasHeuristicProdProp
        data.append(tmp_heuristic)
    return data

def completeWithWater(formulation):
    totalQuantity = 0.0
    completingWater = onto.Dosage(f"dosage_{uuid.uuid4()}")
    completingWater.hasIngredient = [onto.water]

    listDosages = formulation.hasDosage
    for dosage in listDosages:
        if dosage.hasQuantity:
            totalQuantity += dosage.hasQuantity
        if onto.water.iri in dosage.hasIngredient:
            #TODO verifier le comportement
            destroy_entity(completingWater)
            completingWater = dosage
    waterQte = 100.0 - totalQuantity
    completingWater.hasQuantity = float(waterQte)
    formulation.hasDosage.append(completingWater)  

def listerIngredientsPerType():
    data = {}
    Thickeners = onto.Thickener.instances()
    thickenersList = []
    for thickener in Thickeners:
        tmp_thickener = {}
        tmp_thickener['iri'] = thickener.iri
        if thickener.hasINCIcode:
            tmp_thickener['inci'] = thickener.hasINCIcode[0]
        thickenersList.append(tmp_thickener)
    thickenersList.sort(key=lambda d: d['inci'])
    data['thickeners'] = thickenersList

    Surfactants = onto.Surfactant.instances()
    surfactantsList = []
    for surfactant in Surfactants:
        tmp_surfactant = {}
        tmp_surfactant['iri'] = surfactant.iri
        if surfactant.hasINCIcode:
            tmp_surfactant['inci'] = surfactant.hasINCIcode[0]
        surfactantsList.append(tmp_surfactant)
    surfactantsList.sort(key=lambda d: d['inci'])
    data['surfactants'] = surfactantsList

    Emollients = onto.Emollient.instances()
    emollientsList = []
    for emollient in Emollients:
        tmp_emollient = {}
        tmp_emollient['iri'] = emollient.iri
        if emollient.hasINCIcode : 
            tmp_emollient['inci'] = emollient.hasINCIcode[0]
        emollientsList.append(tmp_emollient)
    emollientsList.sort(key=lambda d: d['inci'])
    data['emollients'] = emollientsList

    Actives = onto.Active.instances()
    activesList = []
    for active in Actives:
        tmp_active = {}
        tmp_active['iri'] = active.iri
        if active.hasINCIcode : 
            tmp_active['inci'] = active.hasINCIcode[0]
        activesList.append(tmp_active)
    activesList.sort(key=lambda d: d['inci'])
    data['active'] = activesList
    return data


def calculateOilyPhaseQuantity(formulation):
    oilyPhaseQte = 0.0
    listDosages = formulation.hasDosage
    for dosage in listDosages:
        if len(dosage.hasPhase) and onto.oily_phase.iri in dosage.hasPhase[0].is_a:
            oilyPhaseQte += dosage.hasQuantity
    formulation.hasTotalOilyPhase.append(oilyPhaseQte)

def calculateThickenerQuantity(formulation):
    thickenerQte = 0.0
    listDosages = formulation.hasDosage
    for dosage in listDosages:
        #ings = dosage.hasIngredient
        if onto.Thickener.iri in dosage.hasIngredient[0].is_a:
            thickenerQte += dosage.hasQuantity[0]
    formulation.hasTotalThickenerQuantity.append(thickenerQte) 

def countNbSurfactant(formulation):
    nbSurfactant = 0
    
    listDosages = formulation.hasDosage
    for dosage in listDosages:
        if onto.Surfactant.iri in dosage.hasIngredient[0].is_a:
            nbSurfactant +=1
    formulation.hasNbSurfactantIng.append(nbSurfactant)

def calculateSurfactantQuantity(formulation):
    sufactVol = 0.0
    listDosages = formulation.hasDosage
    for dosage in listDosages:
        #ings = dosage.hasIngredient
        if onto.Surfactant.iri in dosage.hasIngredient[0].is_a:
            sufactVol += dosage.hasQuantity[0]
    formulation.hasTotalSurfactantQuantity = sufactVol

def saveFomulation(ingredients_iri, ingredients_qte):
    if len(ingredients_iri) != len(ingredients_qte):
        raise Exception("IRI array has to have the same size than quantity array")
    else:
        formulationID = uuid.uuid4()
        onto_formulation = get_ontology("http://purl.org/ontocosmetic/temp%s#" % formulationID)
        onto_formulation.imported_ontologies.append(onto)

        with onto_formulation:
            new_formul = onto.Formulation(f"fomulation_{formulationID}")
            for i in range(len(ingredients_iri)):
                tmp_dosage = onto.Dosage(f"dosage_{uuid.uuid4()}")
                print(tmp_dosage)
                ing = IRIS[ingredients_iri[i]]
                print(ing)
                tmp_dosage.hasIngredient.append(ing)
                tmp_dosage.hasQuantity = float(ingredients_qte[i])
                new_formul.hasDosage.append(tmp_dosage)
            completeWithWater(new_formul)
            calculateThickenerQuantity(new_formul)
            calculateSurfactantQuantity(new_formul)
            countNbSurfactant(new_formul)
            #calculateOilyPhaseQuantity(new_formul)
            #sync_reasoner_pellet([onto, onto_formulation], infer_property_values = True, infer_data_property_values = True, debug=2)
            onto_formulation.save(file=f"./app/static/OntoCosmetic-formul_{formulationID}.owl", format = "rdfxml")

def actionOnFormulation(iri, ONTO_ID, action):
    onto_tmp = get_ontology("http://purl.org/ontocosmetic/temp%s#" % ONTO_ID)

    Formulation = IRIS[iri]

    
    if action == "water":
        completeWithWater(Formulation)
    elif action =="reasoning":
        with onto_tmp:
            sync_reasoner_pellet([onto, onto_tmp], infer_property_values = True, infer_data_property_values = True)
    elif action =="thickenerQte":
        with onto_tmp:
            calculateThickenerQuantity(Formulation)
    elif action =="surfactantQte":
        calculateSurfactantQuantity(Formulation)
    elif action =="surfactantNb":
        countNbSurfactant(Formulation)
    elif action =="save":
        with onto_tmp:
            onto_tmp.save(file="./app/static/OntoCosmetic-temp.owl", format = "rdfxml")
            onto.save(file="./app/static/OntoCosmetic-temp_1.owl", format = "rdfxml")
    else:
        pass
