from extras.scripts import *

from dcim.models import Site
from dcim.choices import SiteStatusChoices
from ipam.models import Prefix
from ipam.choices import PrefixStatusChoices


class clean_up(Script):
    class Meta:
        name = "Cleanup"

    def run(self, data, commit):
        for site in Site.objects.filter(status=SiteStatusChoices.STATUS_RETIRED):  
            for prefix in Prefix.objects.filter(site=data['site_name']):
                prefix.status=PrefixStatusChoices.STATUS_DEPRECATED
                prefix.save()
                self.log_success(f"Updated Status of Prexix {prefix}")
                self.log_success("finish")
  
