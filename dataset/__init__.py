from .zjumocap import ZJUMoCapDataset
from .people_snapshot import PeopleSnapshotDataset
from .people_snapshot_multiple import PeopleSnapshotMultipleDataset
from .people_snapshot_mix import PeopleSnapshotMixDataset

def load_dataset(cfg, split='train'):
    dataset_dict = {
        'zjumocap': ZJUMoCapDataset,
        'people_snapshot': PeopleSnapshotDataset,
        'people_snapshot_multiple': PeopleSnapshotMultipleDataset,
        'people_snapshot_mix': PeopleSnapshotMixDataset,
    }
    return dataset_dict[cfg.name](cfg, split)
