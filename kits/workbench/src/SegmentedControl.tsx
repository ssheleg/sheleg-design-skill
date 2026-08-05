export interface SegmentedOption {
  value: string;
  label: string;
}

export interface SegmentedControlProps {
  options: SegmentedOption[];
  value: string;
  onChange: (value: string) => void;
  /** The group's accessible name — "Time range", "Environment". */
  label?: string;
  className?: string;
}

export function SegmentedControl({
  options,
  value,
  onChange,
  label,
  className,
}: SegmentedControlProps) {
  return (
    <div
      className={['wb-seg', className].filter(Boolean).join(' ')}
      role="group"
      aria-label={label}
    >
      {options.map((option) => (
        <button
          key={option.value}
          type="button"
          className="wb-seg__opt"
          aria-pressed={option.value === value}
          onClick={() => onChange(option.value)}
        >
          {option.label}
        </button>
      ))}
    </div>
  );
}
