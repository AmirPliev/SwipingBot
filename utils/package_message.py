

def format_results(results):
    final_string = "*Good day!* I have tried to swipe again and here are my _results_: \n\n"
    for bot, result in results.items():
        final_string += f"*{bot}*:\n"
        for name, score in result.items():
            final_string += f"_{name}_: {score}\n"

        final_string += f"\n"
    return final_string


def test_format():
    test = {
        "TinderBot": {
            "Likes": 0,
            "Swipes": 0,
            "Matches": 0,
        },
        "BumbleBot": {
            "Likes": 0,
            "Swipes": 0,
            "Matches": 0,
        }
    }

    format_results(test)
    