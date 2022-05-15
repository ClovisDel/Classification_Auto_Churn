import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

# variable booléenne ?
def is_binary(list_binary, nom_column):
    if nom_column in list_binary:
        return True
    else:
        return False


class Symbolique:
    def __init__(self, emplacementFichierCSV_IMPORT, emplacementFichierCSV_EXPORT):
        self.df_data = pd.read_csv(emplacementFichierCSV_IMPORT)
        self.list_binary = self.df_data.columns[self.df_data.isin([0, 1, float('nan')]).all()]
        self.nom_column = self.df_data.columns.tolist()
        self.export = emplacementFichierCSV_EXPORT

    # Création des classes pour chaque variables
    def creation_Collonnes(self, element, nbClasses):
        for i in range(0, nbClasses):
            self.df_data[element + "-" + str(i)] = 0

    # retourne les indexes des 2 classes pour les booléens
    def Index_2_Classes(self, collonne):
        # False
        classe1 = self.df_data.index[(self.df_data[collonne] == 0)]
        # True
        classe2 = self.df_data.index[(self.df_data[collonne] == 1)]

        return classe1, classe2

    # retourne les indexes des 3 classes
    def Index_3_Classes(self, collonne):
        max_collone = self.df_data[collonne].max()
        min_collone = self.df_data[collonne].min()
        # std = df_data[collonne].std()
        # moy = df_data[collonne].mean()

        borne1 = (max_collone - min_collone) / 3 + min_collone
        borne2 = (2 / 3) * (max_collone - min_collone) + min_collone

        # borne1 = moy - std
        # borne2 = moy + std

        classe1 = self.df_data.index[(self.df_data[collonne] < borne1)]
        classe3 = self.df_data.index[(self.df_data[collonne] > borne2)]
        classe2 = ((self.df_data.index ^ classe1) ^ classe3)

        return classe1, classe2, classe3

    def export_fichiers(self):
        #Transformation Pandas
        self.df_data = pd.get_dummies(self.df_data)

        # Export en Csv
        self.df_data.to_csv(self.export, index=False, sep=';')
        print(f"Fichier {self.export} exporté !")

    def Variables_To_Symbolique(self):
        # parcour chaque collone de notre dataframe (excepté la dernière)
        for element in self.nom_column[:-1]:
            # Si la variable est non binaire
            if not is_binary(self.list_binary, element):

                # creation_Collonnes(element, 3)
                (x, y, z) = self.Index_3_Classes(element)
                for i in x:
                    self.df_data.at[i, element] = element + "-1"
                for i in y:
                    self.df_data.at[i, element] = element + "-2"
                for i in z:
                    self.df_data.at[i, element] = element + "-3"


            # Si la variable est binaire ==> 2 classes
            else:
                # creation_Collonnes(element, 2)
                (x, y) = self.Index_2_Classes(element)
                for i in x:
                    self.df_data.at[i, element] = element + "-1"
                for i in y:
                    self.df_data.at[i, element] = element + "-2"
            print(f"Collonne Traité {element}pour le jeu de donnée {self.export}")


JeuEntrainement = Symbolique("churner_train_data_set.csv", "Train_Var_Symbolique.csv")
JeuEntrainement.Variables_To_Symbolique()
JeuEntrainement.export_fichiers()

JeuTest = Symbolique("churner_test_data_set.csv", "Test_Var_Symbolique.csv")
JeuTest.Variables_To_Symbolique()
JeuTest.export_fichiers()
