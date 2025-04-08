# main.py

import models as m
import utils as mlb


def main():
    response: m.LookupTeamResponse = mlb.lookup_team(lookup_value="Tigers")
    print(response.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
