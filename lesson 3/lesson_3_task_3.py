from address import Address
from mailing import Mailing

to_address = Address(123432, "SPb", "Новая ул.", 35, 185)
from_address = Address(1743, "Tbi", "Gldani", 63, 24)
mailing = Mailing(4683, "GE574298OL", to_address, from_address)

mailing.display_info()

