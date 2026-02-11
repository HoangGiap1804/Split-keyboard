import board

from kb import KMKKeyboard, isRight; keyboard = KMKKeyboard()
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.keys import KC
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.modules.holdtap import HoldTap; keyboard.modules.append(HoldTap())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.combos import Combos, Chord, Sequence
combos = Combos()
keyboard.modules.append(combos)

split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT

data_pin = board.GP0
data_pin2 = board.GP13

split = Split(
    split_side=split_side,
    split_type=SplitType.UART,
    split_flip=False,
    split_target_left=not isRight,
    use_pio=True,
    data_pin=data_pin,
    data_pin2=data_pin2
)
keyboard.modules.append(split)

BASE = 0
SYM = 1
NUM = 2
NAV = 3
FUN = 4
FUN_MOD = 5

keyboard.keymap = [
    [
        KC.GRAVE,   KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.BSPC,

        KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSLASH,
        
        KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,               KC.H,       KC.J,       KC.K,       KC.L,       KC.SCOLON,  KC.ENTER,
        
        KC.ESC,     KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,               KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.DELETE,
        
        KC.TRNS,    KC.LSHIFT,  KC.LCTL,    KC.LGUI,    KC.SPC,     KC.MO(1),           KC.MO(1),   KC.SPC,     KC.RALT,    KC.RCTL,    KC.RSHIFT,  KC.TRNS
    ],
    [
        KC.GRAVE,   KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.BSPC,
        
        KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,               KC.Y,       KC.U,       KC.MINUS,   KC.EQUAL,   KC.LBRACKET,KC.RBRACKET,
        
        KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,               KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   KC.QUOTE,   KC.ENTER,
        
        KC.ESC,     KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,               KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.DELETE,
        
        KC.TRNS,    KC.LSHIFT,  KC.LCTL,    KC.LGUI,    KC.SPC,     KC.MO(1),           KC.MO(1),   KC.SPC,     KC.RALT,    KC.RCTL,    KC.RSHIFT,  KC.TRNS
    ],

]

layer_names_list = [
    "BASE"
]

if __name__ == '__main__':
     print('starting KMK')
     keyboard.go()
