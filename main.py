from src.specie import Specie
from src.birds_data_manager import BirdDataManager
from src.image import Image
from src.image_uploader import ImageUploader
from src.repository.birds_of_the_world_images_table import BirdsOfTheWorldImagesTable
from src.taxonomy_code import TaxonomyCode

class BirdsOfTheWorld:
    def __init__(self):
        pass

    def run(self):
        specie = Specie()
        taxonomy_list = self.get_taxonomy_list()

        for url in taxonomy_list:
            print(f"URL: {url}")
            species = specie.get_species(url)
            self.process_images(species)

    def get_taxonomy_list(self):
        filename = "/var/www/elt-birds-of-the-world/birdsoftheworld_taxonomy_code.json"
        taxonomy = TaxonomyCode(filename)
        taxonomy_list = taxonomy.get_taxonomy_list()
        return taxonomy_list

    def process_images(self, species):
        bird_data_manager = BirdDataManager()
        uploader = ImageUploader()
        for e in species:

            if bird_data_manager.cientific_name_exists(e['nm_cientifico']):
                print(f"Nome científico '{e['nm_cientifico']}' já exite no arquivo json. Pulando.")
                continue
            
            image = Image(e['ds_imagem_url'], e['nm_arquivo'])
            if image.download_image():
                bird_data_manager.add_bird_data(e['nm_cientifico'], e['ds_imagem_url'], e['nm_arquivo'], e['nm_gcp_path'])

                local_file_path = f"images/{ e['nm_arquivo']}"
                uploader.upload_image(local_file_path)

        table = BirdsOfTheWorldImagesTable()
        table.load_json_into_bq(bird_data_manager.filename)

if __name__ == "__main__":
    botw = BirdsOfTheWorld()
    botw.run()