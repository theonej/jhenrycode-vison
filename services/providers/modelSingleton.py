from keras.models import load_model

class modelSingleton(object):
    m_Model = None

    def __init__(self):
        raise RuntimeError('this is a singleton.  cannot instantiate directly')

    @classmethod
    def instance(cls):
        if cls.m_Model is None:
            cls.m_Model = load_model('../models/trained/weights/plant_maturity.h5')
        return cls.m_Model
