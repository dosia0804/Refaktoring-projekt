# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_items(self):
        for item in self.items:
            self.update_sellin(item)
            self.update_quality(item)

    def update_sellin(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

    def update_quality(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            self.update_legendary_quality(item)
        elif item.name == "Aged Brie":
            self.update_cheese_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass_quality(item)
        elif "Conjured" in item.name:
            self.update_conjured_quality(item)
        else:
            self.update_default_quality(item)

    def modify_quality(self, item, value):
        if item.quality + value > 50:
            item.quality = 50
        elif item.quality + value < 0:
            item.quality = 0
        else:
            item.quality+=value

    def update_legendary_quality(self, item):
        return

    def update_cheese_quality(self, item):
        if item.sell_in < 0:
            self.modify_quality(item, 2)
        else:
            self.modify_quality(item, 1)

    def update_backstage_pass_quality(self, item):
        if item.sell_in < 10:
            self.modify_quality(item, 2)
        elif item.sell_in < 5:
            self.modify_quality(item, 3)
        elif item.quality < 0:
            self.modify_quality(item, -item.quality)
        else:
            self.modify_quality(item, 1)

    def update_default_quality(self, item):
        if item.sell_in < 0:
            self.modify_quality(item, -2)
        else:
            self.modify_quality(item, -1)

    def update_conjured_quality(self, item):
        if item.sell_in < 0:
            self.modify_quality(item, -4)
        else:
            self.modify_quality(item, -2)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
