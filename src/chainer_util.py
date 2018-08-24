import chainer
from chainer import training
from chainer.training import extensions


BATCHSIZE = 300
EPOCH = 500


def get_iter(train, test, batchsize=BATCHSIZE):
    train_iter = chainer.iterators.SerialIterator(train, batch_size=batchsize)
    test_iter = chainer.iterators.SerialIterator(test, batch_size=batchsize,
                                                 repeat=False, shuffle=False)
    return train_iter, test_iter


def save_model(model_path, model):
    print('save model to:{}'.format(model_path))
    model.to_cpu()
    chainer.serializers.save_hdf5(model_path, model, compression=4)


def load_model(model_path, model):
    chainer.serializers.load_hdf5(model_path, model)


def get_trainer(model, train_iter, test_iter, loss_func=None, epoch=EPOCH,
                report='', progress_bar=False):
    # Setup an optimizer
    optimizer = chainer.optimizers.Adam()
    optimizer.setup(model)

    if not loss_func:
        loss_func = model.get_loss_func()

    # Set up an updater
    updater = training.updaters.StandardUpdater(
        train_iter, optimizer, loss_func=loss_func)
    trainer = training.Trainer(updater, (epoch, 'epoch'))
    trainer.extend(extensions.Evaluator(test_iter, model,
                                        eval_func=loss_func))
    trainer.extend(extensions.dump_graph('main/loss'))
    trainer.extend(extensions.LogReport())

    if report == '':
        report = ['epoch', 'main/loss', 'validation/main/loss', 'elapsed_time']

    trainer.extend(extensions.PrintReport(report))

    if progress_bar:
        trainer.extend(extensions.ProgressBar())

    return trainer