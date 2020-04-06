---
layout: post
title: "Design Principles and Design Patterns"
tags: book-notes programming
---

### The Book
This is a really concise article/chapter on software design principles and
patterns by Robert C. Martin (commonly called Uncle Bob). The pdf version of
this book/chapter is available
[here](https://fi.ort.edu.uy/innovaportal/file/2032/1/design_principles.pdf)

### Summary
* software arch is multi-tiered
  * At the highest level, there are the architecture patterns that define the
    overall shape and structure of software applications.
  * Down a level is the architecture that is specifically related to the purpose
    of the software application.
  * Yet another level down resides the architecture of the modules and their
    interconnections. This is the domain of design patterns, packages,
    components, and classes.
* four symptoms of rotting design: rigidity, fragility, immobility, and
  viscosity.
  * rigidity: tendency for the sw to be difficult to change
  * fragility: tendency of sw to break at many places even on a simple change
  * immobility: inability to reuse parts of other or the same project
  * viscosity of design: when design preserving solutions are harder to
    implement than hacks
  * viscosity of environment: development environment is inefficient
* reasons for sw rot
  * changing reqs
  * bad dependency management
* OCP: open closed principle
  * A module should be open for extension but closed for modification
  * the most important rule of sw design
  * abstraction is the key to OCP
  * achieved through runtime and static polymorphism
* If you don’t have to change working code, you aren’t likely to break it.
* LSP: liskov substitution principle
  * Subclasses should be substitutable for their base classes.
  * best paradox for this is circle/ellipse dillema
    * designing circle to inherit from ellipse is fine
    * but users of this code will ruin everything when one wants to pass
      ellipse-like args to a circle object! (think about foci)
  * thus the contract of base class must be obeyed by the child class
* contract of a method consists of precondition and postcondtion
* restating LSP in terms of contracts
  * derived class is substitutable for its base class if:
    * Its preconditions are no stronger than the base class method.
    * Its postconditions are no weaker than the base class method.
    * in other words, derived methods should expect no more and provide no less.
* violations of LSP are latent violations of OCP
* DIP: dependency inversion principle
  * Depend upon Abstractions. Do not depend upon concretions.
  * If the OCP states the goal of OO architecture, the DIP states the primary
    mechanism.
  * No dependency should target a concrete class.
  * concrete things change alot, abstract things change much less frequently
  * abstractions are "hinge points", they represent the places where the design
    can bend or be extended, without themselves being modified (OCP)
* ISP: interface segregation principle. Many client specific interfaces are
  better than one general purpose interface
* PCP: package cohesion principles
  * REP: release reuse equivalency principle
    * The granule of reuse is the granule of release.
  * CCP: common closure principle
    * Classes that change together, belong together.
  * CRP: common reuse principle
    * Classes that aren’t reused together should not be grouped together.
  * these three principles are mutually exclusive. All of them cannot be
    simultaneously satisfied
* PCP: package coupling principles
  * ADP: acyclic dependencies principle
    * The dependencies betwen packages must not form cycles
    * Cycles can be broken in two ways. The first involves creating a new
      package, and the second makes use of the DIP and ISP
    * Interfaces are very often included in the package that uses them, rather
      than in the package that implements them.
* SDP: stable dependencies principle
  * Depend in the direction of stability.
  * package stability measurement
    * Ca = Afferent Coupling. The number of classes outside the package that
      depend upon classes inside the package. (i.e. incoming dependencies)
    * Ce = Efferent Coupling. The number of classes outside the package that
      classes inside the package depend upon. (i.e. outgoing dependencies)
    * I = instability = Ce/(Ca+Ce)
  * Depend upon packages whose I metric is lower than yours
* SAP: stable abstractions principle
  * Stable packages should be abstract packages.
  * compose application from instable packages that are easy to change, and
    stable packages that are easy to extend.
  * abstractness metric:
    * Nc = Number of classes in the package.
    * Na = Number of abstract classes in the package. Remember, an abstract
      class is a class with at least one pure interface, and cannot be instantiated.
    * A Abstractness = Na / Nc
  * I should increase as A decreases
* two zones in the IA graph
  * upper right corner = zone of uselessness = only abstract classes
  * lower left corner = zone of pain = lots of dependencies = only concrete
    classes
  * maximizing distance between these two zones gives us a line called main
    sequence
  * ideally our packages should sit on this line
* distance metric
  * D = Distance from main sequence = |A+I-1|/sqrt(2). This ranges
    from [0,~0.707].
  * D' = Normalized Distance = |A+I-1|. This metric is much more convenient than
    D since it ranges from [0,1]. Zero indicates that the package is directly on
    the main sequence. One indicates that the package is as far away as possible
    from the main sequence.
* design patterns = repeating structures of design and architecture
* abstract server: when client depends directly on server DIP is violated. Thus
  create an interface which client uses but server implements
* adapter: delegator of methods from an abstract interface to the third party
  server implementation
* observer: when changes in one object needs to be informed to another without
  each knowing much about the other
* bridge: base and child classes are tightly coupled. This creates a strong
  separation between interface and implementation
* abstract factory: DIP strongly recommends that modules not depend upon
  concrete classes. However, in order ot create an instance of a class, you must
  depend upon the concrete class. This allows that dependency upon the concrete
  class to exist in one, and only one, place.
