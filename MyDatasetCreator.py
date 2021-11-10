if __name__ == "__main__":
    from ProceduralData import *

    def Create():
        dataset_loader = DatasetLoader()
        dataset_dictionary:dict = dataset_loader.LoadDatasetFromJSON("./Datasets/Downloaded_datasets/" + dataset_name + ".json")
        sorted_dataset:dict = dataset_loader.SortDictionary(dataset_dictionary)

        my_complete_dataset_object = DatasetsGenerator(sorted_dataset=sorted_dataset, few_shot_range=(0,3), dataset_training_size=100_000, dataset_other_size=1_000)
        my_complete_dataset:dict = my_complete_dataset_object.Create()

        DatasetLoader.SaveDataset(dataset_dictionary=my_complete_dataset, save_directory="./Datasets/My_datasets/",  file_name="my_"+dataset_name)

    dataset_name:str = "ag_news_dataset"
    Create()
    dataset_name:str = "emotion_dataset"
    Create()
    dataset_name:str = "yelp_polarity_dataset"
    Create()
    dataset_name:str = "kan_hope_dataset"
    Create()