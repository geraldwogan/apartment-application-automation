import pytest

@pytest.mark.parametrize("link", ['https://www.daft.ie/for-rent/apartment-bronze-en-suite-2022-23-tenancy-41-weeks-brickworks-brickfield-lane-dublin-8/2863979'])
def test_completeForm(link):
    assert link == 'https://www.daft.ie/for-rent/apartment-bronze-en-suite-2022-23-tenancy-41-weeks-brickworks-brickfield-lane-dublin-8/2863979'