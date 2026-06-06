import pytest
import main

def test_novalogger_instantiation():
    # Verify that the class NovaLogger is inspectable and loadable
    assert hasattr(main, 'NovaLogger')

