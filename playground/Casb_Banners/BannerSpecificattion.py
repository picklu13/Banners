import abc
class InputContext():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_tenant_name(self):
        raise NotImplementedError()


class TenantDataContext(InputContext):

    def __init__(self, tenant_data_dict):
        self.tenant_name = tenant_data_dict["name"]
        # self.other_detail = tenant_data_dict["somekey"]

    def get_tenant_name(self):
        return self.tenant_name


class BannerCriterion:

    __metaclass__ = abc.ABCMeta

    def __init__(self, input_context):
        self.input_context = input_context

    def set_input_context(self, input_context):
        self.input_context = input_context

    def get_input_context(self):
        return self.input_context

    @abc.abstractproperty
    def banner_data_response(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_satisfied(self):
        pass


class Category1BannerCondition(BannerCriterion):

    def __init__(self, input_context):
        tenant_input_context = TenantDataContext(input_context)
        super(Category1BannerCondition, self).__init__(tenant_input_context)

    def is_satisfied(self):
        return True

    @property
    def banner_data_response(self):
        return {"text" : "Category 1 Banner"}


class BannerDriver():

    def list_banners(self):
        list_of_banners = []
        subs = BannerCriterion.__subclasses__()
        ip_dict = {"name": "tenant_name"}
        for sub in subs:
            obj = sub(ip_dict)
            if obj.is_satisfied():
                list_of_banners.append(obj.banner_data_response)
        return list_of_banners



print BannerDriver().list_banners()




