#!/usr/bin/env python3

import yaml
import re
import logging

class VarItem:

    name = "" # Variable name
    description = "" # Variable description
    type = "" # Variable type
    line = "" # Line of variable