from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline


training_path: str = "kg/train.hrt.txt"
validation_path: str = "kg/valid.hrt.txt"
testing_path: str = "kg/test.hrt.txt"


training = TriplesFactory(
    path=training_path,
)
valid = TriplesFactory(
    path=validation_path,
    entity_to_id=training.entity_to_id,
    relation_to_id=training.relation_to_id,
)
testing = TriplesFactory(
    path=testing_path,
    entity_to_id=training.entity_to_id,
    relation_to_id=training.relation_to_id,
)

result = pipeline(
    training=training,
    validation=valid,
    testing=testing,
    model='TransE',
    training_kwargs=dict(num_epochs=2, batch_size=512),
    evaluation_kwargs=dict(batch_size=128)
)
result.save_to_directory('saved-model')


import torch
model = torch.load('saved-model/trained_model.pkl')
print(model.predict_heads('VARIANT_DISEASE_associated', 'Leigh_syndrome'))
