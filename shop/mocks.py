import requests
 
# l'ecoscore est stockÃ© dans une constante et sera rÃ©utilisÃ© dans nos tests
ECOSCORE_GRADE = 'd'
 
def mock_openfoodfact_success(self, method, url):
    # Notre mock doit avoir la mÃªme signature que la mÃ©thode Ã  mocker
    # Ã€ savoir les paramÃ¨tres d'entrÃ©e et le type de sortie
    def monkey_json():
    # Nous crÃ©ons une mÃ©thode qui servira Ã  monkey patcher response.json()
        return {
            'product': {
            'ecoscore_grade': ECOSCORE_GRADE
            }
        }
 
    # CrÃ©ons la rÃ©ponse et modifions ses valeurs pour que le status code et les donnÃ©es
    # correspondent Ã  nos attendus
    response = requests.Response()
    response.status_code = 200
    # Nous monkey patchons response.json
    # Attention Ã  ne pas mettre les (), nous n'appelons pas la mÃ©thode mais la remplaÃ§ons
    response.json = monkey_json
    return response