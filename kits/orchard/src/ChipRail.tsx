export interface ChipRailItem {
  id: string;
  label: string;
}

export interface ChipRailProps {
  items: ChipRailItem[];
  /**
   * The id of the selected item. There is always exactly one — the rail has no
   * empty state, because "no filter" is itself one of the items.
   */
  selected: string;
  onSelect: (id: string) => void;
  /** The group's accessible name — "Symptoms", "What it is for". */
  label?: string;
  className?: string;
}

export function ChipRail({ items, selected, onSelect, label, className }: ChipRailProps) {
  return (
    <div
      className={['orch-rail', className].filter(Boolean).join(' ')}
      role="group"
      aria-label={label}
    >
      {items.map((item) => (
        <button
          key={item.id}
          type="button"
          className={[
            'orch-chip',
            'orch-chip--neutral',
            'orch-rail__chip',
            item.id === selected ? 'orch-chip--selected' : undefined,
          ]
            .filter(Boolean)
            .join(' ')}
          aria-pressed={item.id === selected}
          onClick={() => onSelect(item.id)}
        >
          {item.label}
        </button>
      ))}
    </div>
  );
}
