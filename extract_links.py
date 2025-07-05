import re
import quopri


class LinkExtractor(object):
    @staticmethod
    def extract_links(email_text):
        """Extracts meal plan titles and links grouped by category."""
        decoded_text = quopri.decodestring(email_text).decode("utf-8", errors="ignore")

        category_pattern = re.compile(
            r"For (breakfast|lunch|dinner|snacking|dessert) this week, I'm making:",
            re.IGNORECASE,
        )

        meal_plan = {}
        current_category = None
        current_recipe = None

        lines = decoded_text.split("\n")
        for line in lines:
            line = line.strip()

            match = category_pattern.search(line)
            if match:
                current_category = match.group(1).capitalize()
                meal_plan[current_category] = {}
                continue

            if line.startswith("* "):
                current_recipe = line.lstrip("* ").strip()
                continue

            if current_recipe and "(" in line and "http" in line:
                raw_link = re.search(
                    r"\(\s*(https?://[^\s)]+(?:=[\n\s]*[^\s)]+)*)\s*\)", line
                )
                if raw_link:
                    cleaned_link = raw_link.group(1).replace("=\n", "").replace("=", "")
                    if current_category:
                        meal_plan[current_category][current_recipe] = cleaned_link
                    current_recipe = None

        return meal_plan
