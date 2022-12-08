from src.image_ops import read_img, show_img
from src.template_matching import match_template_to_img, match_template_to_img_size_invariant


def test_template_matching(img_path, template_path, threshold=0.8,best_only=True):
    test_img = read_img(img_path)
    test_template = read_img(template_path)
    result = match_template_to_img(test_img, test_template, threshold, best_only)
    show_img(f'showing found matches of {template_path} in {img_path}', result)

def test_size_invariant_template_matching(img_path, template_path, threshold=0.8,best_only=True):
    test_img = read_img(img_path)
    test_template = read_img(template_path)
    result = match_template_to_img_size_invariant(test_img, test_template, threshold, best_only)
    show_img(f'showing found matches of {template_path} in {img_path}', result)