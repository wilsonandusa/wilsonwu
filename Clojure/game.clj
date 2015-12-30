(ns adventure.core
  (:require [clojure.core.match :refer [match]]
          [clojure.string :as str])
  (:gen-class))

(def the-map
  {:foyer {:desc "The walls are freshly painted but do not have
                 any pictures.  You get the feeling it was just
                 created for some game or something."
           :title "in the foyer"
           :dir {:north :hallway
                 :south :grue-pen
                 :east  :office
                 :down  :basement}
           :content #{:raw-egg}
           }

   :grue-pen {:desc "There is a grue here.  You are about to get eaten."
              :title "the grue pen"
              :dir {:north :foyer}
              :content #{:grue}}
   :hallway {:desc "It is very short, but not too short."
              :title "the hallway"
              :dir {:south :foyer
                    :north :kitchen
                    :west :bedroom1
                    :east :bedroom2}
              :content #{}}
   :kitchen {:desc "It looks like you could cook food here. Type cook [item] to cook it."
              :title "the kitchen"
              :dir {:south :hallway
                    :west :diningRoom
                    :east :livingRoom}
              :content #{}}
  :livingRoom {:desc "there is a guest waiting for you. try talking to him"
           :title "the living room"
           :dir {:west :kitchen
                 :east :balcony}
            :content #{}}
  :balcony {:desc "the view is beautiful. enjoy the fresh air"
              :title "the balcony"
              :dir {:west :livingRoom}
              :content #{}}
    :diningRoom {:desc "have some food. get focused!"
                 :title "the dining room"
                 :dir {:east :kitchen}
                 :content #{:sandwhich}}
    :bedroom1 {:desc "There is bed. Type sleep to go to sleep."
               :title "the first bedroom"
               :dir {:east :hallway
                     :west :bathroom}
                :content #{:sword}}
    :bathroom {:desc "I heard the water is warm. Trying talking a shower"
               :title "the bathroom"
               :dir {:east :bedroom1}
               :content #{}}
    :bedroom2 {:desc "There is a bed. Type sleep to go to sleep. tip: check your dresser"
               :title "the second bedroom"
               :dir {:east :kidsRoom
                     :west :hallway}
                :content #{:armor}}
    :kidsRoom {:desc "be quite the kids are sleeping!"
               :title "the kids room"
               :dir {:west :bedroom2}
               :content #{:key}}
    :basement {:desc "Watch out from the monster. Type fight to fight it!"
               :title "the basement"
               :dir {:up :foyer
                    :west :storage}
               :content #{}}
    :storage {:desc "There is a treasure. Type 'open' to open it."
              :title "the storage room"
              :dir {:east :basement}
              :content #{}}
    :office {:desc "you have a lot of work to do"
             :title "the office"
             :dir {:west :foyer}
             :content #{:map}}

  } )

(def adventurer {
  :location :foyer
  :inventory #{}
  :before #{}
  :condition :awake
  :monsterCondition :alive
  })

(def theMentor {
  :location :livingRoom
  :message "To kill the monster you need the sword located in bedroom one"
  })

(defn pickItems [item adv]
  (if (= (get-in adv [:condition]) :sleeping)
    (do (println "You can't pick items while you are sleeping. Type 'wakeup' to wakeup") adv)
  (let [curr-room (get-in adv [:location])]
    (let [currItems (get-in (get-in the-map [curr-room]) [:content])]
      (if (or (empty? currItems) (= (contains? currItems item) false))
        (do (println "Can't pickup this item," item) adv)
        (do (println "You picked" item)(update-in adv [:inventory] #(conj % item)))
  )))))

(defn dropItems [item adv]
  (if (= (get-in adv [:condition]) :sleeping)
    (do (println "You can't drop items while you are sleeping. Type 'wakeup' to wakeup") adv)
  (let [curr-inventory (get-in adv [:inventory])]
    (if (or (empty? curr-inventory) (= (contains? curr-inventory item) false))
      (do (println "You can't drop" item) adv)
    (do (println "You can pick it up from the same location.")
      (assoc-in adv [:inventory] (disj curr-inventory item)))
  ))))

(defn open [adv item]
  (if (= (get-in adv [:condition]) :sleeping)
    (do (println "You can't open items while you are sleeping. Type 'wakeup' to wakeup") adv)
  (let [curr-room (get-in adv [:location])]
  (if (not (= curr-room :storage))
    (do (println "The treasure is located at the storage room.") adv)
  (let [curr-inventory (get-in adv [:inventory])]
  (if (= (contains? curr-inventory :key) false)
    (do (println "You should have a key to open the treasure. Hint: check the kid's room.") adv)
  (do (println "You opened the treasure box.") adv)
  ))))))

(defn sleep [adv]
  (let [curr-room (get-in adv [:location])]
  (let [currCondition (get-in adv [:condition])]
  (let [newCondition :sleeping]
  (if (and (not (= curr-room :bedroom1)) (not (= curr-room :bedroom2)))
    (do (println "You can only sleep in bedroom 1 or bedroom2.") adv)
    (do
      (if (= currCondition newCondition)
        (do (println "You are already sleeping type wakeup to wake up") adv)
        (do (println "Sweet dreams") (assoc-in adv [:condition] newCondition))
      )))))))

(defn wakeup [adv]
  (let [curr-room (get-in adv [:location])]
  (let [currCondition (get-in adv [:condition])]
  (let [newCondition :awake]
    (if (= currCondition newCondition)
        (do (println "You are already awake.") adv)
        (do (println "Had a good sleep ?") (assoc-in adv [:condition] newCondition))
      )))))

(defn talkToMentor [adv mentor]
  (if (= (get-in adv [:condition]) :sleeping)
    (do (println "You can't talk to a mentor while you are sleeping.") adv)
  (let [curr-room (get-in adv [:location])]
  (let [mentor-room (get-in mentor [:location])]
  (if (not (= curr-room mentor-room))
    (do (println "The mentor is located in" mentor-room) adv)
  (do (println "Mentor's Message:"(get-in mentor [:message])) adv)
  )))))

(defn fightMonster [adv]
  (if (= (get-in adv [:condition]) :sleeping)
    (do (println "You can't fight a monster while you are sleeping.") adv)
  (let [curr-room (get-in adv [:location])]
  (let [monster-condition (get-in adv [:monsterCondition])]
    (if (not (= curr-room :basement))
      (do (println "The monster is located at the basement") adv)
    (if (= monster-condition :dead)
      (do (println "The monster is already dead") adv)
    (if (= (contains? (get-in adv [:inventory]) :sword) false)
      (do (println "You need the sword that is located at bedroom 1 to kill the monster") adv)
    (do (println "The monster is dead")
      (assoc-in adv [:monsterCondition] :dead)
  ))))))))

(defn theContent [location]
  (if (empty? (-> the-map location :content)) (println "There are no content.")
    (println "The contents are" (-> the-map location :content))))

(defn status [adv]
  (let [location (adv :location)]
    (println (str "You are at " (-> the-map location :title)))
    (when-not ((adv :before) location)
      (println (-> the-map location :desc) ))
    (theContent location)
    (println "the inventory:" (adv :inventory))
    (println "The adventurer condition is" (adv :condition))
    (update-in adv [:before] #(conj % location))))

(defn go [dir adv]
  (if (= (get-in adv [:condition]) :sleeping)
    (do (println "You are sleeping. Type wakeup to wake up") adv)
  (let [curr-room (get-in adv [:location])]
   (if-let [dest (get-in the-map [curr-room :dir dir])]
   (if (and (= dest :storage) (= (get-in adv [:monsterCondition]) :alive))
    (do (println "You need to kill the monster first.") adv)
      (assoc-in adv [:location] dest))
     (do (println "You cannot go that direction.") adv)
     ) )))

(defn printMap [adv]
(let [curr-inventory (get-in adv [:inventory])]
  (if (= (contains? curr-inventory :map) false)
    (do (println "You need to find the map. Hint: check the office.") adv)
(do (println "
          Dining Room  - -  Kitchen - - Living Room - - Balcony
                              |          (mentor)
                              |
Bathroom - - Bedroom 1 - -  Hallway - - Bedroom 2 - - Kid's room
                              |
                              |
                            Foyer - - office
                          /   |
    Storage - - basement      |
                (monster)   Grue Pen
                     ") adv))))

(defn eatSomething [adv item]
  (if (= (get-in adv [:condition]) :sleeping)
    (do (println "You can't eat items while you are sleeping. Type 'wakeup' to wakeup") adv)
  (if (and (not (= item :raw-egg)) (not (= item :sandwhich)))
    (do (println "You can't eat" item) adv)
  (let [curr-inventory (get-in adv [:inventory])]
    (if (= (contains? curr-inventory item) false)
      (do (println item "is not in your inventory") adv)
    (do (println "You just ate" item)
      (dropItems item adv)
  ))))))


(defn respond [inst adv]
  (match inst
         [:north] (go :north adv)
         [:south] (go :south adv)
         [:west] (go :west adv)
         [:east] (go :east adv)
         [:down] (go :down adv)
         [:up] (go :up adv)
         [:status] (do (print "") adv)
         [:sleep] (sleep adv)
         [:wakeup] (wakeup adv)
         [:pick item] (pickItems item adv)
         [:drop item] (dropItems item adv)
         [:pick] (do (println "Type pick [item]") adv)
         [:drop] (do (println "Type drop [item]") adv)
         [:fight] (fightMonster adv)
         [:talk] (talkToMentor adv theMentor)
         [:map] (printMap adv)
         [:eat item] (eatSomething adv item)
         [:eat] (do (println "Type eat [item]") adv)
         [:open] (open adv :treasure)
         _ (do
             (println "I'm sorry Dave.  I cannot allow you to do that.")
             adv) ) )

(defn to-keywords [st]
   (mapv keyword (str/split st #" +")))

(defn -main
  [& args]
  (println "Welcome to the Uncooked Egg Adventure!")
  (loop [the-m the-map
         the-a adventurer]
    (let [the-a' (status the-a)
          _      (println "What do you want to do?")
          inst   (read-line) ]
      (recur the-m (respond (to-keywords inst) the-a'))
      ) ) )
