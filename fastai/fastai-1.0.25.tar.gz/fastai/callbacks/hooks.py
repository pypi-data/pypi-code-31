"Hooks provide extensibility at the model level."
from ..torch_core import *
from ..callback import *
from ..basic_train import *
from ..basic_data import *

__all__ = ['ActivationStats', 'Hook', 'HookCallback', 'Hooks', 'hook_output', 'hook_outputs', 
           'model_sizes', 'num_features_model']

class Hook():
    "Create a hook."
    def __init__(self, m:nn.Module, hook_func:HookFunc, is_forward:bool=True, detach:bool=True):
        self.hook_func,self.detach,self.stored = hook_func,detach,None
        f = m.register_forward_hook if is_forward else m.register_backward_hook
        self.hook = f(self.hook_fn)
        self.removed = False

    def hook_fn(self, module:nn.Module, input:Tensors, output:Tensors):
        if self.detach:
            input  = (o.detach() for o in input ) if is_listy(input ) else input.detach()
            output = (o.detach() for o in output) if is_listy(output) else output.detach()
        self.stored = self.hook_func(module, input, output)

    def remove(self):
        if not self.removed:
            self.hook.remove()
            self.removed=True

class Hooks():
    "Create several hooks."
    def __init__(self, ms:Collection[nn.Module], hook_func:HookFunc, is_forward:bool=True, detach:bool=True):
        self.hooks = [Hook(m, hook_func, is_forward, detach) for m in ms]

    def __getitem__(self,i:int) -> Hook: return self.hooks[i]
    def __len__(self) -> int: return len(self.hooks)
    def __iter__(self): return iter(self.hooks)
    @property
    def stored(self): return [o.stored for o in self]

    def remove(self):
        for h in self.hooks: h.remove()

def hook_output (module:nn.Module) -> Hook:  return Hook (module,  lambda m,i,o: o)
def hook_outputs(modules:Collection[nn.Module]) -> Hooks: return Hooks(modules, lambda m,i,o: o)

class HookCallback(LearnerCallback):
    "Callback that registers given hooks."
    def __init__(self, learn:Learner, modules:Sequence[nn.Module]=None, do_remove:bool=True):
        super().__init__(learn)
        self.modules,self.do_remove = modules,do_remove

    def on_train_begin(self, **kwargs):
        if not self.modules:
            self.modules = [m for m in flatten_model(self.learn.model)
                            if hasattr(m, 'weight')]
        self.hooks = Hooks(self.modules, self.hook)

    def on_train_end(self, **kwargs):
        if self.do_remove: self.remove()

    def remove(self): self.hooks.remove()
    def __del__(self): self.remove()

class ActivationStats(HookCallback):
    "Callback that record the activations."
    def on_train_begin(self, **kwargs):
        super().on_train_begin(**kwargs)
        self.stats = []

    def hook(self, m:nn.Module, i:Tensors, o:Tensors) -> Tuple[Rank0Tensor,Rank0Tensor]:
        return o.mean().item(),o.std().item()
    def on_batch_end(self, train, **kwargs): 
        if train: self.stats.append(self.hooks.stored)
    def on_train_end(self, **kwargs): self.stats = tensor(self.stats).permute(2,1,0)

def model_sizes(m:nn.Module, size:tuple=(64,64), full:bool=True) -> Tuple[Sizes,Tensor,Hooks]:
    "Pass a dummy input through the model to get the various sizes. Returns (res,x,hooks) if `full`"
    hooks = hook_outputs(m)
    ch_in = in_channels(m)
    x = next(m.parameters()).new(1,ch_in,*size)
    x = m.eval()(x)
    res = [o.stored.shape for o in hooks]
    if not full: hooks.remove()
    return (res,x,hooks) if full else res

def num_features_model(m:nn.Module)->int:
    "Return the number of output features for `model`."
    return model_sizes(m, full=False)[-1][1]
