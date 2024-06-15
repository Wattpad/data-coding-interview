import csv
from datetime import date
from pathlib import Path

from . import models

import logging
logger = logging.getLogger(__name__)


def transform(
    output_stories_author_csv_p: Path,
    stories_csv_p: Path,
    users_csv_p: Path,
    modified_dt: date
):
    """
    Joins records from stories_csv_p [models.Story] with the users_csv_p [models.User] records
    on `Story.author_id=User.id`. Only Story records that that have been modified on the given
    modified_dt date [Story.modified_ts=modified_dt] are selected.

    The result is then outputted as CSV to output_stories_author_csv_p [models.StoryAuthor].
    """

    with stories_csv_p.open() as stories_csv_f, \
            users_csv_p.open() as users_csv_f, \
            output_stories_author_csv_p.open('w') as output_f:

        output_w = csv.DictWriter(output_f, models.StoryAuthor.model_fields.keys())
        output_w.writeheader()

        # List used to track rows that will be outputted
        output_rows = []

        stories_csv_r = csv.DictReader(stories_csv_f)
        for story_row in stories_csv_r:
            story = models.Story(**story_row)

            if story.modified_ts.date() != modified_dt:
                continue

            # We use a brute-force linear search of the users_csv to find the matching
            # user.id to join with the story.author_id. We therefore need to
            # reset the users_csv_f location to the beginning of the file.
            users_csv_f.seek(0)
            users_csv_r = csv.DictReader(users_csv_f)

            for user_row in users_csv_r:
                user = models.User(**user_row)
                if user.id == story.author_id:
                    story_author = models.StoryAuthor(
                        id=story.id,
                        title=story.title,
                        summary=story.summary,
                        author_id=user.id,
                        author_name=user.name,
                        author_profile=user.profile,
                        author_email=user.email)
                    output_rows.append(dict(story_author))

        output_w.writerows(output_rows)
