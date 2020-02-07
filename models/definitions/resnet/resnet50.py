from keras.models import Sequential, Model

from keras.layers import Input, Conv2D, MaxPooling2D, AveragePooling2D, Activation, BatchNormalization, Dropout, Flatten, Dense, Add, ZeroPadding2D

from keras.initializers import glorot_uniform

def create_model(input_shape, classes):
    X_Input = Input(input_shape)

    X = ZeroPadding2D((3,3))(X_Input)

    X = Conv2D(64, (7,7), strides=(2,2), name='conv1', kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_conv1')(X)
    X = Activation('relu')(X)
    X = MaxPooling2D((3,3), strides=(2,2))(X)

    filters = [64, 64, 256]
    X = convolutional_block(X, f=3, filters=filters, stage=2, block='a', stride=1)
    X = identity_block(X, 3, filters, stage=2, block='b')
    X = identity_block(X, 3, filters, stage=2, block='c')

    filters = [128, 128, 512]
    X = convolutional_block(X, f=3, filters=filters, stage=3, block='a', stride=1)
    X = identity_block(X, 3, filters, stage=3, block='b')
    X = identity_block(X, 3, filters, stage=3, block='c')
    X = identity_block(X, 3, filters, stage=3, block='d')
    
    filters = [256, 256, 1024]
    X = convolutional_block(X, f=3, filters=filters, stage=4, block='a', stride=1)
    X = identity_block(X, 3, filters, stage=4, block='b')
    X = identity_block(X, 3, filters, stage=4, block='c')
    X = identity_block(X, 3, filters, stage=4, block='d')
    X = identity_block(X, 3, filters, stage=4, block='e')
    X = identity_block(X, 3, filters, stage=4, block='f')

    filters = [512, 512, 2048]
    X = convolutional_block(X, f=3, filters=filters, stage=5, block='a', stride=1)
    X = identity_block(X, 3, filters, stage=5, block='b')
    X = identity_block(X, 3, filters, stage=5, block='c')

    X = AveragePooling2D(pool_size=(2,2), padding='same')(X)

    X = Flatten()(X)
    X = Dense(classes, activation='softmax', name='fully_connected1', kernel_initializer=glorot_uniform(seed=0))(X)

    model = Model(inputs=X_Input, outputs = X, name='Resnet50')

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model


def identity_block(X, f, filters, stage, block):
    conv_name_base = 'res{}{}_branch'.format(stage, block)
    batch_norm_name_base = 'bn{}{}_branch'.format(stage, block)

    F1,F2,F3 = filters

    X_residual = X

    X = Conv2D(filters=F1, kernel_size=(1,1), strides=(1,1), padding='valid', name='{}2a'.format(conv_name_base), kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='{}2a'.format(batch_norm_name_base))(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=F2, kernel_size=(f,f), strides=(1,1), padding='same', name='{}2b'.format(conv_name_base), kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='{}2b'.format(batch_norm_name_base))(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=F3, kernel_size=(1,1), strides=(1,1), padding='valid', name='{}2c'.format(conv_name_base), kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='{}2c'.format(batch_norm_name_base))(X)

    #add residual back in
    X = Add()([X, X_residual])

    X = Activation('relu')(X)

    return X

def convolutional_block(X, f, filters, stage, block, stride=2):
    conv_name_base = 'res{}{}_branch'.format(stage, block)
    batch_norm_name_base = 'bn{}{}_branch'.format(stage, block)

    F1,F2,F3 = filters

    X_residual = X

    X = Conv2D(filters=F1, kernel_size=(1,1), strides=(stride,stride), padding='valid', name='{}2a'.format(conv_name_base), kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='{}2a'.format(batch_norm_name_base))(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=F2, kernel_size=(f,f), strides=(1,1), padding='same', name='{}2b'.format(conv_name_base), kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='{}2b'.format(batch_norm_name_base))(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=F3, kernel_size=(1,1), strides=(1,1), padding='valid', name='{}2c'.format(conv_name_base), kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='{}2c'.format(batch_norm_name_base))(X)

    #residual path
    X_residual = Conv2D(filters=F3, kernel_size=(1,1), strides=(stride,stride), padding='valid', name='{}1'.format(conv_name_base), kernel_initializer=glorot_uniform(seed=0))(X_residual)
    X_residual = BatchNormalization(axis=3, name='{}1'.format(batch_norm_name_base))(X_residual)

    X = Add()([X, X_residual])
    X = Activation('relu')(X)

    return X