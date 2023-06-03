from typing import Dict, Type

from app.generator_pages import GeneratorPage
from app.generator_pages.normal_generator_page import NormalGeneratorPage
from app.generator_pages.uniform_generator_page import UniformGeneratorPage

MAP_PAGES: Dict[str, Type[GeneratorPage]] = {
    "Normal distribution": NormalGeneratorPage,
    "Uniform distribution": UniformGeneratorPage
}