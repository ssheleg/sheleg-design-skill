export interface FieldProps {
  label: string;
  name: string;
  type?: 'text' | 'email' | 'search';
  placeholder?: string;
  /** The message shown beside the invalid border — the colour never travels alone. */
  error?: string;
  className?: string;
}

export function Field({ label, name, type = 'text', placeholder, error, className }: FieldProps) {
  const described = error !== undefined ? `${name}-error` : undefined;
  return (
    <div className={['dm-field', className].filter(Boolean).join(' ')}>
      <label className="dm-field__label" htmlFor={name}>
        {label}
      </label>
      <input
        className="dm-field__input"
        id={name}
        name={name}
        type={type}
        placeholder={placeholder}
        aria-invalid={error !== undefined || undefined}
        aria-describedby={described}
      />
      {error !== undefined && (
        <p className="dm-field__error" id={described}>
          {error}
        </p>
      )}
    </div>
  );
}
